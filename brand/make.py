"""Generate the AnywidgetInstruments visual identity.

Writes the SVG logos and banners of this directory, then the PNG exports
when `rsvg-convert` is available. Edit the palette or the geometry here and
run `python3 brand/make.py`; never edit the generated files by hand.
"""

from __future__ import annotations

import math
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Palette: the colours of the widgets' own light and dark themes.
LIGHT = {
    "ink": "#111827",
    "muted": "#4b5563",
    "face": "#f9fafb",
    "tick": "#9ca3af",
    "bands": ("#1e3a8a", "#2563eb", "#f59e0b"),
}
DARK = {
    "ink": "#f9fafb",
    "muted": "#9ca3af",
    "face": "#111827",
    "tick": "#4b5563",
    "bands": ("#93c5fd", "#60a5fa", "#fbbf24"),
}

FONT = "Inter, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace"

START, SWEEP = 225.0, 270.0  # dial arc: from bottom left, clockwise over the top
GAP = 6.0  # degrees between two bands
NEEDLE = 62.0  # needle angle, in the second band


def point(cx: float, cy: float, r: float, deg: float) -> tuple[float, float]:
    a = math.radians(deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def arc(cx: float, cy: float, r: float, a0: float, a1: float) -> str:
    """Clockwise arc from angle a0 down to a1 (degrees, a0 > a1)."""
    x0, y0 = point(cx, cy, r, a0)
    x1, y1 = point(cx, cy, r, a1)
    large = 1 if a0 - a1 > 180 else 0
    return f"M{x0:.2f} {y0:.2f}A{r} {r} 0 {large} 1 {x1:.2f} {y1:.2f}"


def mark(p: dict, cx: float = 64, cy: float = 64, s: float = 1.0) -> str:
    """The dial: three bands (industrial, automotive, aeronautics), ticks, needle."""
    r, w = 46 * s, 11 * s
    step = SWEEP / 3
    out = []
    for i, colour in enumerate(p["bands"]):
        a0 = START - i * step - (GAP / 2 if i else 0)
        a1 = START - (i + 1) * step + (GAP / 2 if i < 2 else 0)
        out.append(
            f'<path d="{arc(cx, cy, r, a0, a1)}" fill="none" stroke="{colour}" '
            f'stroke-width="{w:.2f}"/>'
        )
    for k in range(11):
        a = START - k * SWEEP / 10
        x0, y0 = point(cx, cy, 29 * s, a)
        x1, y1 = point(cx, cy, (34 if k % 5 else 36) * s, a)
        out.append(
            f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" '
            f'stroke="{p["tick"]}" stroke-width="{3 * s:.2f}" stroke-linecap="round"/>'
        )
    tip = point(cx, cy, 38 * s, NEEDLE)
    back = point(cx, cy, 9 * s, NEEDLE + 180)
    out.append(
        f'<line x1="{back[0]:.2f}" y1="{back[1]:.2f}" x2="{tip[0]:.2f}" y2="{tip[1]:.2f}" '
        f'stroke="{p["ink"]}" stroke-width="{5 * s:.2f}" stroke-linecap="round"/>'
    )
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{8 * s:.2f}" fill="{p["ink"]}"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{3 * s:.2f}" fill="{p["bands"][2]}"/>')
    return "\n  ".join(out)


def svg(w: int, h: int, body: str, title: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="{title}">\n'
        f"  <title>{title}</title>\n  {body}\n</svg>\n"
    )


def wordmark(p: dict, x: float, y: float, size: float) -> str:
    return (
        f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
        f'letter-spacing="-0.5" fill="{p["ink"]}">'
        f'<tspan fill="{p["muted"]}" font-weight="400">anywidget</tspan>'
        f'<tspan font-weight="700">instruments</tspan></text>'
    )


def logo(p: dict) -> str:
    body = mark(p, 64, 64) + "\n  " + wordmark(p, 140, 80, 44)
    return svg(560, 128, body, "anywidget instruments")


def avatar(p: dict) -> str:
    body = f'<rect width="128" height="128" fill="{p["face"]}"/>\n  ' + mark(p, 64, 71)
    return svg(128, 128, body, "anywidget instruments")


def banner(p: dict) -> str:
    families = "industrial  ·  automotive  ·  aeronautics"
    hosts = "Python  ·  Julia  ·  Jupyter  ·  marimo  ·  Grafana"
    body = "\n  ".join(
        [
            f'<rect width="1280" height="320" fill="{p["face"]}"/>',
            mark(p, 190, 160, 2.0),
            wordmark(p, 340, 150, 68),
            f'<text x="343" y="202" font-family="{FONT}" font-size="26" fill="{p["muted"]}">'
            "Instrument panels for notebooks, dashboards and the web</text>",
            f'<text x="344" y="252" font-family="{MONO}" font-size="19" fill="{p["bands"][1]}">'
            f"{families}</text>",
            f'<text x="344" y="282" font-family="{MONO}" font-size="19" fill="{p["muted"]}">'
            f"{hosts}</text>",
        ]
    )
    return svg(1280, 320, body, "anywidget instruments")


def social(p: dict) -> str:
    """The 1280 x 640 image GitHub shows when a repository link is shared."""
    inner = banner(p).split("\n", 2)[2].rsplit("</svg>", 1)[0]
    body = (
        f'<rect width="1280" height="640" fill="{p["face"]}"/>\n  '
        f'<g transform="translate(0 160)">{inner}</g>'
    )
    return svg(1280, 640, body, "anywidget instruments")


# Link icons, 24 x 24 outlines: documentation, source code, live demo.
ICONS = {
    "docs": '<path d="M3 5h5a4 4 0 0 1 4 4v11a3 3 0 0 0-3-3H3zM21 5h-5a4 4 0 0 0-4 4v11a3 3 0 0 1 3-3h6z"/>',
    "code": '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
    "try": '<circle cx="12" cy="12" r="9.5"/><path d="M10 8.5v7l6-3.5z"/>',
}
ICON_COLOUR = "#3b82f6"  # readable on both GitHub themes


def icon(name: str, colour: str = ICON_COLOUR, x: float = 0, y: float = 0, s: float = 1.0) -> str:
    return (
        f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{colour}" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>'
    )


def button(p: dict, name: str, label: str) -> str:
    """A link button: outlined pill, icon and label, sized to the label."""
    w = round(70 + len(label) * 8.7)
    colour = p["bands"][1]
    body = "\n  ".join(
        [
            f'<rect x="1" y="1" width="{w - 2}" height="46" rx="10" fill="{p["face"]}" '
            f'stroke="{colour}" stroke-width="2"/>',
            icon(name, colour, 18, 12),
            f'<text x="52" y="30.5" font-family="{FONT}" font-size="17" font-weight="600" '
            f'fill="{p["ink"]}">{label}</text>',
        ]
    )
    return svg(w, 48, body, label)


BUTTONS = {
    "try": ("try", "Try in the browser"),
    "docs-industrial": ("docs", "Industrial docs"),
    "docs-automotive": ("docs", "Automotive docs"),
    "docs-aeronautics": ("docs", "Aeronautics docs"),
    "docs-grafana": ("docs", "Grafana panel docs"),
}


def main() -> None:
    files = {
        "logo-light.svg": logo(LIGHT),
        "logo-dark.svg": logo(DARK),
        "mark-light.svg": svg(128, 128, mark(LIGHT), "anywidget instruments"),
        "mark-dark.svg": svg(128, 128, mark(DARK), "anywidget instruments"),
        "avatar.svg": avatar(DARK),
        "banner-light.svg": banner(LIGHT),
        "banner-dark.svg": banner(DARK),
        "social-preview.svg": social(DARK),
    }
    for name in ICONS:
        files[f"icons/{name}.svg"] = svg(24, 24, icon(name), name)
    for key, (name, label) in BUTTONS.items():
        files[f"buttons/{key}-light.svg"] = button(LIGHT, name, label)
        files[f"buttons/{key}-dark.svg"] = button(DARK, name, label)
    for name, text in files.items():
        (HERE / name).parent.mkdir(exist_ok=True)
        (HERE / name).write_text(text, encoding="utf-8")
    if shutil.which("rsvg-convert"):
        exports = [("avatar.svg", "avatar.png", 512), ("social-preview.svg", "social-preview.png", 1280)]
        for src, dst, width in exports:
            subprocess.run(
                ["rsvg-convert", "-w", str(width), "-o", str(HERE / dst), str(HERE / src)],
                check=True,
            )


if __name__ == "__main__":
    main()
