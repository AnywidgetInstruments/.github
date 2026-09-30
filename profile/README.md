<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/banner-dark.svg">
  <img alt="anywidget instruments: instrument panels for notebooks, dashboards and the web" src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/banner-light.svg">
</picture>

**Instrument panels for notebooks, dashboards and the web.** Knobs, gauges,
tanks, LEDs, switches, strip charts and alarm annunciators for industrial
processes; speedometers, tachometers, tell-tales and clusters for vehicles;
flight instruments next. Built on [anywidget](https://anywidget.dev), usable
from Python, Julia and Grafana.

**Website: <https://anywidgetinstruments.github.io/>**

<p>
<a href="https://anywidgetinstruments.github.io/try/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/buttons/try-dark.svg"><img alt="Try in the browser" src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/buttons/try-light.svg" height="40"></picture></a>
<a href="https://anywidgetinstruments.github.io/anywidget-instruments-industrial/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/buttons/docs-industrial-dark.svg"><img alt="Industrial documentation" src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/buttons/docs-industrial-light.svg" height="40"></picture></a>
<a href="https://anywidgetinstruments.github.io/anywidget-instruments-automotive/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/buttons/docs-automotive-dark.svg"><img alt="Automotive documentation" src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/buttons/docs-automotive-light.svg" height="40"></picture></a>
<a href="https://anywidgetinstruments.github.io/afm-host-panel/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/buttons/docs-grafana-dark.svg"><img alt="Grafana panel documentation" src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/buttons/docs-grafana-light.svg" height="40"></picture></a>
</p>

The [demos](https://anywidgetinstruments.github.io/try/) run in the browser (Python through Pyodide): nothing to install.

## One front end, many hosts

Each widget is a TypeScript front-end module driven by a set of **traits**
described by a JSON Schema contract. Everything a widget displays, unit
conversion included, is computed in the front end; a host only sets traits.
The same widget therefore behaves alike in JupyterLab, Jupyter Notebook,
marimo, VS Code, Colab, Pluto, standalone HTML pages and Grafana dashboards.

## Instrument families

<img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/docs.svg" width="14" alt=""> documentation &nbsp;
<img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/try.svg" width="14" alt=""> live demos &nbsp;
<img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/code.svg" width="14" alt=""> source code

| Family | Links | Conventions | Status |
|---|---|---|---|
| **Core**<br><sub>anywidget-instruments</sub> | <a href="https://anywidgetinstruments.github.io/anywidget-instruments/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/docs.svg" width="20" alt="Documentation"></a> <a href="https://github.com/AnywidgetInstruments/anywidget-instruments"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/code.svg" width="20" alt="Source code"></a> | | base view and class, trait contract, themes, liveness; every family builds on it |
| **Industrial**<br><sub>anywidget-instruments-industrial</sub> | <a href="https://anywidgetinstruments.github.io/anywidget-instruments-industrial/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/docs.svg" width="20" alt="Documentation"></a> <a href="https://anywidgetinstruments.github.io/anywidget-instruments-industrial/try/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/try.svg" width="20" alt="Live demos"></a> <a href="https://github.com/AnywidgetInstruments/anywidget-instruments-industrial"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/code.svg" width="20" alt="Source code"></a> | ISA-101, IEC 60073, ISA-18.2 | pre-alpha, 52 widgets |
| **Automotive**<br><sub>anywidget-instruments-automotive</sub> | <a href="https://anywidgetinstruments.github.io/anywidget-instruments-automotive/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/docs.svg" width="20" alt="Documentation"></a> <a href="https://github.com/AnywidgetInstruments/anywidget-instruments-automotive"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/code.svg" width="20" alt="Source code"></a> | UN R121, ISO 2575, ISO 15008 | early implementation |
| **Aeronautics**<br><sub>anywidget-instruments-aeronautics</sub> | <a href="https://anywidgetinstruments.github.io/anywidget-instruments-aeronautics/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/docs.svg" width="20" alt="Documentation"></a> <a href="https://anywidgetinstruments.github.io/anywidget-instruments-aeronautics/try/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/try.svg" width="20" alt="Live demos"></a> <a href="https://github.com/AnywidgetInstruments/anywidget-instruments-aeronautics"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/code.svg" width="20" alt="Source code"></a> | CS-23 / CS-25, AC 25-11 | early implementation: the basic six |

## Hosts

| Host | Links | |
|---|---|---|
| **Python**<br><sub>anywidget-instruments-industrial</sub> | <a href="https://anywidgetinstruments.github.io/anywidget-instruments-industrial/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/docs.svg" width="20" alt="Documentation"></a> <a href="https://github.com/AnywidgetInstruments/anywidget-instruments-industrial"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/code.svg" width="20" alt="Source code"></a> | Jupyter, marimo and every anywidget host |
| **Julia**<br><sub>Anywidget.jl</sub> | <a href="https://anywidgetinstruments.github.io/Anywidget.jl/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/docs.svg" width="20" alt="Documentation"></a> <a href="https://github.com/AnywidgetInstruments/Anywidget.jl"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/code.svg" width="20" alt="Source code"></a> | anywidget front-end modules in Julia: standalone HTML, Jupyter, Pluto, Kaimon Slate |
| **Julia**<br><sub>AnywidgetInstruments.jl</sub> | <a href="https://anywidgetinstruments.github.io/AnywidgetInstruments.jl/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/docs.svg" width="20" alt="Documentation"></a> <a href="https://github.com/AnywidgetInstruments/AnywidgetInstruments.jl"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/code.svg" width="20" alt="Source code"></a> | the instruments, hosted by Anywidget.jl |
| **Grafana**<br><sub>afm-host-panel</sub> | <a href="https://anywidgetinstruments.github.io/afm-host-panel/"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/docs.svg" width="20" alt="Documentation"></a> <a href="https://github.com/AnywidgetInstruments/afm-host-panel"><img src="https://raw.githubusercontent.com/AnywidgetInstruments/.github/main/brand/icons/code.svg" width="20" alt="Source code"></a> | a panel plugin running anywidget front-end modules, instruments built in |

## Safety

These widgets are for visualization, teaching, simulation and supervision
dashboards. They are **not** certified instruments: they must not replace the
safety functions of a plant, the instruments of a vehicle or those of an
aircraft.

<sub>All projects are in initial development. Contributions and feedback are
welcome in each repository.</sub>
