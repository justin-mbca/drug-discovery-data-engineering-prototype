from google.cloud import bigquery

project_id = "my-fastapi-demo-490623"
dataset_id = "drug_discovery_demo"

client = bigquery.Client(project=project_id)

# List of old tables to delete
old_tables = [
    "benchling_data",
    "cdd_vault_data",
    "mosaic_inventory",
]

for table_name in old_tables:
    table_ref = f"{project_id}.{dataset_id}.{table_name}"
    try:
        client.delete_table(table_ref, not_found_ok=True)
        print(f"Deleted table {table_ref} (if it existed).")
    except Exception as e:
        print(f"Error deleting table {table_ref}: {e}")
