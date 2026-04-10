# Financial Crises Signal Atlas

This project explores and visualizes major financial crises of the past century using a consistent **4-phase signal framework**:

1. **Pre-crisis build-up**
2. **Cracks appear**
3. **Systemic break**
4. **Real-economy spillover**

The goal is not to be only 2008-focused. The repository is structured so we can compare multiple crises with the same indicator logic.

## Project Structure

- `data/reference/`: crisis catalog, phase windows, event timeline, and indicator metadata
- `data/raw/`: raw downloaded series (FRED and other sources)
- `data/processed/`: harmonized analysis-ready panel
- `notebooks/`: analysis notebooks following the 4-phase structure
- `docs/`: methodology and roadmap
- `scripts/`: reproducible data pipeline utilities
- `src/`: reusable helper functions
- `archive/legacy_2008/`: original project artifacts preserved for traceability

## Quick Start

1. Create and activate local environment:
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`
2. Run full data pipeline:
   - `./scripts/run_pipeline.sh`
3. Open:
   - `notebooks/01_multi_crisis_signal_dashboard.ipynb`
   - `notebooks/02_cross_crisis_phase_comparison.ipynb`

## Dataset Metadata

- Crisis list: `data/reference/crisis_catalog.csv`
- Phase windows: `data/reference/crisis_phase_windows.csv`
- Event markers: `data/reference/timeline_events.csv`
- Indicator registry: `data/reference/fred_series_catalog.csv`

## Current Baseline Coverage

- Fully wired baseline notebook for:
  - Global Financial Crisis (2008)
  - Dot-com Crash (2000-2002)
  - Asian Financial Crisis (1997-1998)
- Cross-crisis aligned phase comparison notebook:
  - compare `pre_crisis`, `cracks`, `system_break`, `spillover` on month-aligned timelines
- Expandable to additional crises through metadata tables.
