from google.cloud import bigquery

project_id = "my-fastapi-demo-490623"
dataset_id = "drug_discovery_demo"

client = bigquery.Client(project=project_id)

tables = {
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

for table_name, schema in tables.items():
    table_ref = f"{project_id}.{dataset_id}.{table_name}"
    try:
        client.delete_table(table_ref, not_found_ok=True)
        print(f"Deleted table {table_ref} (if it existed).")
    except Exception as e:
        print(f"Error deleting table {table_ref}: {e}")
    table = bigquery.Table(table_ref, schema=schema)
    try:
        client.create_table(table)
        print(f"Table {table_ref} created.")
    except Exception as e:
        print(f"Error creating table {table_ref}: {e}")
