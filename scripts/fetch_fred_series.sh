#!/usr/bin/env bash
set -euo pipefail

CATALOG_PATH="${1:-data/reference/fred_series_catalog.csv}"
OUTPUT_DIR="${2:-data/raw/fred}"

if [[ ! -f "$CATALOG_PATH" ]]; then
  echo "Catalog not found: $CATALOG_PATH" >&2
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo "Downloading FRED series listed in $CATALOG_PATH"
awk -F, 'NR>1 {print $1}' "$CATALOG_PATH" | while read -r series_id; do
  [[ -z "$series_id" ]] && continue
  url="https://fred.stlouisfed.org/graph/fredgraph.csv?id=${series_id}"
  out_file="$OUTPUT_DIR/${series_id}.csv"
  echo "- ${series_id}"
  curl -fsSL "$url" -o "$out_file"
done

echo "Done. Files saved to $OUTPUT_DIR"
