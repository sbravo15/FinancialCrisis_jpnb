import pandas as pd
from pathlib import Path


def load_series_catalog(path: Path) -> pd.DataFrame:
    """Load the indicator metadata table."""
    return pd.read_csv(path)


def load_fred_series(raw_dir: Path, series_id: str) -> pd.DataFrame:
    """Load one raw FRED CSV and standardize columns."""
    df = pd.read_csv(raw_dir / f"{series_id}.csv")
    value_col = series_id
    if value_col not in df.columns:
        raise ValueError(f"Expected column '{series_id}' in series file for {series_id}")

    df = df.rename(columns={"observation_date": "date", value_col: "value"})
    df["date"] = pd.to_datetime(df["date"])
    df["series_id"] = series_id
    return df[["date", "series_id", "value"]]
