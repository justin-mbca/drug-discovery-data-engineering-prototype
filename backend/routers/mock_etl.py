
from fastapi import APIRouter
import threading

# In-memory mock BigQuery tables
mock_bigquery = {
    "cdd": [],
    "mosaic": [],
    "benchling": []
}

# Lock for thread safety
mock_etl_lock = threading.Lock()

router = APIRouter()

@router.get("/etl/analytics/available_compounds")
def analytics_available_compounds():
    """Join CDD and Mosaic to show compounds with available samples."""
    with mock_etl_lock:
        cdd = {row["compound_id"]: row for row in mock_bigquery["cdd"]}
        available_samples = [row for row in mock_bigquery["mosaic"] if row["status"].lower() == "available"]
        result = []
        for sample in available_samples:
            compound = cdd.get(sample["compound_id"])
            if compound:
                result.append({
                    "compound_id": compound["compound_id"],
                    "compound_name": compound["name"],
                    "sample_id": sample["sample_id"],
                    "location": sample["location"],
                    "quantity": sample["quantity"],
                    "unit": sample["unit"]
                })
        return {"available_compounds": result}

@router.get("/etl/analytics/experiments_by_compound")
def analytics_experiments_by_compound():
    """Aggregate experiment results by compound from Benchling."""
    with mock_etl_lock:
        # Group experiments by compound_id
        experiments = {}
        for row in mock_bigquery["benchling"]:
            cid = row["compound_id"]
            if cid not in experiments:
                experiments[cid] = []
            experiments[cid].append({
                "entry_id": row["entry_id"],
                "experiment": row["experiment"],
                "date": row["date"],
                "scientist": row["scientist"],
                "result": row["result"]
            })
        return {"experiments_by_compound": experiments}

@router.post("/etl/run")
def run_etl():
    """
    Simulate ETL: load mock API data into mock BigQuery tables.
    """
    with mock_etl_lock:
        # CDD
        mock_bigquery["cdd"] = [
            {
                "compound_id": "ABC123",
                "name": "Aspirin",
                "structure": "CC(=O)OC1=CC=CC=C1C(=O)O",
                "activity": "Active",
                "project": "Pain Relief"
            },
            {
                "compound_id": "DEF456",
                "name": "Ibuprofen",
                "structure": "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
                "activity": "Inactive",
                "project": "Inflammation"
            },
            {
                "compound_id": "GHI789",
                "name": "Paracetamol",
                "structure": "CC(=O)NC1=CC=C(O)C=C1",
                "activity": "Active",
                "project": "Fever"
            }
        ]
        # Mosaic
        mock_bigquery["mosaic"] = [
            {
                "sample_id": "SMP456",
                "compound_id": "ABC123",
                "location": "Freezer A - Rack 3",
                "quantity": 120,
                "unit": "uL",
                "status": "Available"
            },
            {
                "sample_id": "SMP789",
                "compound_id": "DEF456",
                "location": "Freezer B - Rack 1",
                "quantity": 200,
                "unit": "uL",
                "status": "Depleted"
            },
            {
                "sample_id": "SMP101",
                "compound_id": "GHI789",
                "location": "Freezer C - Rack 2",
                "quantity": 50,
                "unit": "uL",
                "status": "Available"
            }
        ]
        # Benchling
        mock_bigquery["benchling"] = [
            {
                "entry_id": "ELN789",
                "compound_id": "ABC123",
                "experiment": "Enzyme Kinetics",
                "date": "2026-03-18",
                "scientist": "Dr. Jane Doe",
                "result": "Increased activity observed at pH 7.4"
            },
            {
                "entry_id": "ELN790",
                "compound_id": "DEF456",
                "experiment": "Solubility Test",
                "date": "2026-03-19",
                "scientist": "Dr. John Smith",
                "result": "Low solubility in water"
            },
            {
                "entry_id": "ELN791",
                "compound_id": "GHI789",
                "experiment": "Toxicity Assay",
                "date": "2026-03-20",
                "scientist": "Dr. Alice Lee",
                "result": "No toxicity observed"
            }
        ]
    return {"message": "ETL complete. Mock data loaded into mock BigQuery tables."}

@router.get("/etl/tables")
def list_mock_tables():
    """List all mock BigQuery tables and their row counts."""
    with mock_etl_lock:
        return {table: len(rows) for table, rows in mock_bigquery.items()}

@router.get("/etl/table/{table_name}")
def get_mock_table(table_name: str):
    """Get all rows from a mock BigQuery table."""
    with mock_etl_lock:
        if table_name not in mock_bigquery:
            return {"error": f"Table {table_name} not found."}
        return {"rows": mock_bigquery[table_name]}

@router.get("/etl/analytics/summary")
def analytics_summary():
    """Simple analytics: count rows in each table."""
    with mock_etl_lock:
        return {
            "cdd_count": len(mock_bigquery["cdd"]),
            "mosaic_count": len(mock_bigquery["mosaic"]),
            "benchling_count": len(mock_bigquery["benchling"])
        }
