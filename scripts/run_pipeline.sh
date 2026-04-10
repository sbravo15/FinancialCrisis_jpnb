#!/usr/bin/env bash
set -euo pipefail

./scripts/fetch_fred_series.sh
.venv/bin/python scripts/build_indicator_panel.py

echo "Pipeline complete. Open notebooks/01_multi_crisis_signal_dashboard.ipynb"
