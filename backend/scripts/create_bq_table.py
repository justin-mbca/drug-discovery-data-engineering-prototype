import os
from google.cloud import bigquery

# Set these variables to match your GCP setup
PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "my-fastapi-demo-490623")
DATASET_ID = os.environ.get("BQ_DATASET_ID", "your_dataset")
TABLE_ID = os.environ.get("BQ_TABLE_ID", "your_table")


# Schemas for each mock API
SCHEMAS = {
    "benchling": [
        bigquery.SchemaField("entry_id", "STRING"),
        bigquery.SchemaField("experiment", "STRING"),
        bigquery.SchemaField("date", "STRING"),
        bigquery.SchemaField("scientist", "STRING"),
        bigquery.SchemaField("result", "STRING"),
    ],
    "cdd": [
        bigquery.SchemaField("compound_id", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("structure", "STRING"),
        bigquery.SchemaField("activity", "STRING"),
        bigquery.SchemaField("project", "STRING"),
    ],
    "mosaic": [
        bigquery.SchemaField("sample_id", "STRING"),
        bigquery.SchemaField("location", "STRING"),
        bigquery.SchemaField("quantity", "INTEGER"),
        bigquery.SchemaField("unit", "STRING"),
        bigquery.SchemaField("status", "STRING"),
    ],
}

def create_dataset_if_not_exists(client, dataset_id):
    dataset_ref = bigquery.Dataset(f"{PROJECT_ID}.{dataset_id}")
    try:
        client.get_dataset(dataset_ref)
        print(f"Dataset {dataset_id} already exists.")
    except Exception:
        client.create_dataset(dataset_ref)
        print(f"Created dataset {dataset_id}.")


def create_table_if_not_exists(client, dataset_id, table_id, schema):
    table_ref = bigquery.Table(f"{PROJECT_ID}.{dataset_id}.{table_id}", schema=schema)
    try:
        client.get_table(table_ref)
        print(f"Table {table_id} already exists.")
    except Exception:
        client.create_table(table_ref)
        print(f"Created table {table_id}.")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Create BigQuery table for a mock API.")
    parser.add_argument("--schema", choices=["benchling", "cdd", "mosaic"], required=True, help="Which schema to use.")
    args = parser.parse_args()

    client = bigquery.Client(project=PROJECT_ID)
    create_dataset_if_not_exists(client, DATASET_ID)
    create_table_if_not_exists(client, DATASET_ID, TABLE_ID, SCHEMAS[args.schema])


if __name__ == "__main__":
    main()
