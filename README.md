# Financial Crises Signal Atlas

A visualization-first, academically grounded project to study major financial crises through a shared 4-phase framework:

1. **Pre-crisis build-up**
2. **Cracks appear**
3. **Systemic break**
4. **Real-economy spillover**

The goal is to compare crises with the same signal lens, not only to narrate 2008.

## Visual Storyline

Each crisis is read as a timeline of signals:

- **Pre-crisis build-up**: valuations, leverage, and risk-taking conditions are stretched.
- **Cracks appear**: credit quality and funding conditions deteriorate.
- **Systemic break**: market and liquidity stress become nonlinear.
- **Spillover**: labor, production, and confidence absorb the shock.

The notebooks intentionally prioritize visual interpretation while keeping explicit methodological guardrails.

## Academic Guardrails

- **Descriptive, not causal**: charts show co-movements and timing, not proof of causation.
- **Transparent phase windows**: crisis windows are explicitly defined in metadata.
- **Comparable scaling**: z-scores are used for cross-indicator comparison when appropriate.
- **Reproducible pipeline**: raw downloads, transformations, and outputs are scripted.
- **Source traceability**: indicator IDs and event markers are versioned in reference tables.

## Repository Layout

- `data/reference/`: crisis catalog, phase windows, event timeline, indicator registry
- `data/raw/`: raw source series (FRED and other sources)
- `data/processed/`: harmonized analysis-ready panel
- `notebooks/`: visualization and comparison notebooks
- `scripts/`: reproducible data pipeline scripts
- `docs/`: scope and roadmap
- `archive/legacy_2008/`: preserved original project artifacts

## Notebooks (GitHub-Readable Narrative)

1. `notebooks/01_multi_crisis_signal_dashboard.ipynb`
   - crisis-by-crisis visual narrative with phase shading and event markers
2. `notebooks/02_cross_crisis_phase_comparison.ipynb`
   - aligned phase comparisons across crises (`month_from_phase_start = 0`)

## Quick Start

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `./scripts/run_pipeline.sh`
5. Open both notebooks above.

## Data & Metadata

- Crisis definitions: `data/reference/crisis_catalog.csv`
- Phase windows: `data/reference/crisis_phase_windows.csv`
- Event markers: `data/reference/timeline_events.csv`
- Indicator registry: `data/reference/fred_series_catalog.csv`

## Current Crisis Coverage

- Global Financial Crisis (2008)
- Dot-com Crash (2000-2002)
- Asian Financial Crisis (1997-1998)
- Savings and Loan Crisis (phase windows scaffolded; deeper narrative pending)
