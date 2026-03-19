
import requests
from google.cloud import bigquery
import os
import argparse

# Set these variables to match your GCP setup
PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "my-fastapi-demo-490623")
DATASET_ID = os.environ.get("BQ_DATASET_ID", "your_dataset")
TABLE_ID = os.environ.get("BQ_TABLE_ID", "your_table")

# Default deployed Cloud Run base URL
CLOUD_RUN_BASE_URL = os.environ.get(
    "CLOUD_RUN_BASE_URL",
    "https://mock-apis-871527614878.us-central1.run.app"
)

ENDPOINTS = {
    "benchling": f"{CLOUD_RUN_BASE_URL}/benchling/data",
    "cdd": f"{CLOUD_RUN_BASE_URL}/cdd/data",
    "mosaic": f"{CLOUD_RUN_BASE_URL}/mosaic/data",
}

def fetch_data(endpoint):
    url = ENDPOINTS.get(endpoint)
    if not url:
        raise ValueError(f"Unknown endpoint: {endpoint}")
    print(f"Fetching data from {url}")
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    # If the data is nested under a key, flatten it
    if isinstance(data, dict) and endpoint in data:
        data = data[endpoint]
    return data


def get_unique_id_field(endpoint):
    # Map endpoint to unique ID field
    return {
        "benchling": "entry_id",
        "cdd": "compound_id",
        "mosaic": "sample_id",
    }[endpoint]

def get_existing_ids(client, table_ref, id_field):
    query = f"SELECT {id_field} FROM `{table_ref}`"
    query_job = client.query(query)
    return set(row[id_field] for row in query_job)

def insert_data(rows, endpoint):
    client = bigquery.Client(project=PROJECT_ID)
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    if isinstance(rows, dict):
        rows = [rows]
    id_field = get_unique_id_field(endpoint)
    existing_ids = get_existing_ids(client, table_ref, id_field)
    new_rows = [row for row in rows if row.get(id_field) not in existing_ids]
    if not new_rows:
        print("No new rows to insert (all IDs already exist).")
        return
    errors = client.insert_rows_json(table_ref, new_rows)
    if errors:
        print(f"Encountered errors while inserting rows: {errors}")
    else:
        print(f"Inserted {len(new_rows)} new rows successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load mock API data into BigQuery.")
    parser.add_argument("--endpoint", choices=["benchling", "cdd", "mosaic"], required=True, help="Which mock API endpoint to load from.")
    args = parser.parse_args()
    data = fetch_data(args.endpoint)
    insert_data(data, args.endpoint)

# Usage:
# python load_mocked_to_bq.py --endpoint benchling
# python load_mocked_to_bq.py --endpoint cdd
# python load_mocked_to_bq.py --endpoint mosaic

# To automate, schedule this script with cron, Cloud Scheduler, or a CI/CD pipeline.
# To test endpoints, you can also curl them directly:
# curl https://mock-apis-871527614878.us-central1.run.app/benchling/data
