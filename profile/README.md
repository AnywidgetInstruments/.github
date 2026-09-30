<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/banner-dark.svg">
  <img alt="anywidget instruments: instrument panels for notebooks, dashboards and the web" src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/banner-light.svg">
</picture>

**Instrument panels for notebooks, dashboards and the web.** Knobs, gauges,
tanks, LEDs, switches, strip charts and alarm annunciators for industrial
processes; speedometers, tachometers, tell-tales and clusters for vehicles;
flight instruments next. Built on [anywidget](https://anywidget.dev), usable
from Python, Julia and Grafana.

## One front end, many hosts

Each widget is a TypeScript front-end module driven by a set of **traits**
described by a JSON Schema contract. Everything a widget displays, unit
conversion included, is computed in the front end; a host only sets traits.
The same widget therefore behaves alike in JupyterLab, Jupyter Notebook,
marimo, VS Code, Colab, Pluto, standalone HTML pages and Grafana dashboards.

## Instrument families

| Family | Repository | Conventions | Status |
|---|---|---|---|
| Industrial | [anywidget-instruments-industrial](https://github.com/AnywidgetInstruments/anywidget-instruments-industrial) | ISA-101, IEC 60073, ISA-18.2 | pre-alpha, 52 widgets; owns the trait contract |
| Automotive | [anywidget-instruments-automotive](https://github.com/AnywidgetInstruments/anywidget-instruments-automotive) | UN R121, ISO 2575, ISO 15008 | early implementation |
| Aeronautics | — | | planned |

## Hosts

| Host | Repository | |
|---|---|---|
| Python | [anywidget-instruments-industrial](https://github.com/AnywidgetInstruments/anywidget-instruments-industrial) | Jupyter, marimo and every anywidget host |
| Julia | [Anywidget.jl](https://github.com/AnywidgetInstruments/Anywidget.jl) | anywidget front-end modules in Julia: standalone HTML, Jupyter, Pluto, Kaimon Slate |
| Julia | [AnywidgetInstruments.jl](https://github.com/AnywidgetInstruments/AnywidgetInstruments.jl) | the instruments, hosted by Anywidget.jl |
| Grafana | [afm-host-panel](https://github.com/AnywidgetInstruments/afm-host-panel) | a panel plugin running anywidget front-end modules, instruments built in |

## Safety

These widgets are for visualization, teaching, simulation and supervision
dashboards. They are **not** certified instruments: they must not replace the
safety functions of a plant, the instruments of a vehicle or those of an
aircraft.

<sub>All projects are in initial development. Contributions and feedback are
welcome in each repository.</sub>
