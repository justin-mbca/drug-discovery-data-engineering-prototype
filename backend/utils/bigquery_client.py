
from google.cloud import bigquery

def get_bigquery_data():
    # Explicitly set the project ID
    client = bigquery.Client(project="mybigqueryproj-383820")
    query = """
        SELECT table_schema, table_name
        FROM `mybigqueryproj-383820`.information_schema.tables
        WHERE table_schema = 'drug_discovery'
    """
    try:
        query_job = client.query(query)
        results = [dict(row) for row in query_job]
        return {"bigquery": results}
    except Exception as e:
        return {"error": str(e)}
