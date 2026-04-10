#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = PROJECT_ROOT / "data/reference/fred_series_catalog.csv"
RAW_DIR = PROJECT_ROOT / "data/raw/fred"
OUT_PANEL_PATH = PROJECT_ROOT / "data/processed/indicator_panel_monthly.csv"
OUT_WIDE_PATH = PROJECT_ROOT / "data/processed/indicator_panel_monthly_wide.csv"


PHASE_ORDER = {
    "pre_crisis": 1,
    "cracks": 2,
    "system_break": 3,
    "spillover": 4,
    "all_phases": 5,
}


def _to_monthly(values: pd.Series, source_frequency: str) -> pd.Series:
    source_frequency = str(source_frequency).strip().lower()

    if source_frequency in {"daily", "weekly"}:
        monthly = values.resample("MS").mean()
    elif source_frequency == "quarterly":
        monthly = values.resample("MS").ffill()
    else:
        monthly = values.resample("MS").mean()

    return monthly.dropna()


def _load_one_series(row: pd.Series) -> pd.DataFrame:
    series_id = row["series_id"]
    csv_path = RAW_DIR / f"{series_id}.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing raw series file: {csv_path}")

    df = pd.read_csv(csv_path)
    if "observation_date" not in df.columns or series_id not in df.columns:
        raise ValueError(f"Unexpected schema in {csv_path.name}")

    df = df.rename(columns={"observation_date": "date", series_id: "value"})
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["date", "value"]).sort_values("date")

    monthly_values = _to_monthly(df.set_index("date")["value"], row["frequency"])
    out = monthly_values.rename("value").reset_index()
    out["series_id"] = series_id
    out["indicator_name"] = row["indicator_name"]
    out["domain"] = row["domain"]
    out["phase_default"] = row["phase_default"]
    out["phase_order"] = PHASE_ORDER.get(str(row["phase_default"]), np.nan)
    out["source_frequency"] = row["frequency"]
    out["source"] = row["source"]
    return out


def _add_zscore(panel: pd.DataFrame) -> pd.DataFrame:
    panel = panel.copy()

    def zscore(group: pd.Series) -> pd.Series:
        std = group.std(ddof=0)
        if std == 0 or pd.isna(std):
            return pd.Series(np.zeros(len(group)), index=group.index)
        return (group - group.mean()) / std

    panel["value_z"] = panel.groupby("series_id")["value"].transform(zscore)
    return panel


def main() -> None:
    catalog = pd.read_csv(CATALOG_PATH)
    if catalog.empty:
        raise ValueError("Series catalog is empty")

    frames = [_load_one_series(row) for _, row in catalog.iterrows()]
    panel = pd.concat(frames, ignore_index=True)
    panel = _add_zscore(panel)
    panel = panel.sort_values(["series_id", "date"]).reset_index(drop=True)

    OUT_PANEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    panel.to_csv(OUT_PANEL_PATH, index=False)

    wide = (
        panel.pivot_table(index="date", columns="series_id", values="value", aggfunc="first")
        .sort_index()
        .reset_index()
    )
    wide.to_csv(OUT_WIDE_PATH, index=False)

    coverage = panel.groupby("series_id")["date"].agg(["min", "max", "count"]).reset_index()
    print("Saved:")
    print(f"- {OUT_PANEL_PATH}")
    print(f"- {OUT_WIDE_PATH}")
    print("\nSeries coverage:")
    print(coverage.to_string(index=False))


if __name__ == "__main__":
    main()
