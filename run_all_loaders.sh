#!/bin/bash
# Run all loader jobs for mock endpoints and log output
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export BQ_DATASET_ID=drug_discovery

echo "Loading Benchling..."
export BQ_TABLE_ID=benchling
python3 "$SCRIPT_DIR/backend/scripts/load_mocked_to_bq.py" --endpoint benchling "$@"

echo "Loading CDD..."
export BQ_TABLE_ID=cdd
python3 "$SCRIPT_DIR/backend/scripts/load_mocked_to_bq.py" --endpoint cdd "$@"

echo "Loading Mosaic..."
export BQ_TABLE_ID=mosaic
python3 "$SCRIPT_DIR/backend/scripts/load_mocked_to_bq.py" --endpoint mosaic "$@"

echo "All mock data loaded into BigQuery."
