import os

# CDD Vault API credentials (set these as environment variables)
CDD_API_KEY = os.environ.get("CDD_API_KEY")
CDD_BASE_URL = os.environ.get("CDD_BASE_URL", "https://app.collaborativedrug.com/api/v1")
from fastapi import APIRouter, Response, Request

router = APIRouter()

@router.get("/data")
def get_cdd_data(response: Response, request: Request):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    # Remove ETag if present
    if "etag" in response.headers:
        del response.headers["etag"]
    # Mocked CDD Vault data (multiple unique records)
    return {
        "cdd": [
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
    }
