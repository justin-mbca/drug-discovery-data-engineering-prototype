import os
from fastapi import APIRouter, Response, Request, Query
# CDD Vault API credentials (set these as environment variables)
CDD_API_KEY = os.environ.get("CDD_API_KEY")
CDD_BASE_URL = os.environ.get("CDD_BASE_URL", "https://app.collaborativedrug.com/api/v1")

router = APIRouter()

@router.get("/data")

@router.get("/data")
def get_cdd_data(response: Response, request: Request, page: int = Query(1, ge=1), page_size: int = Query(100, ge=1, le=1000)):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    # Remove ETag if present
    if "etag" in response.headers:
        del response.headers["etag"]
    # Mock data: many records
    mock_data = [
        {"compound_id": f"CMPD{i:04d}", "name": f"Compound {i}", "structure": f"Structure {i}", "activity": "Active" if i%2==0 else "Inactive", "project": f"Project {i%5}"}
        for i in range(1, 201)
    ]
    # Sort by compound_id to ensure stable order
    mock_data = sorted(mock_data, key=lambda x: x["compound_id"])
    start = (page - 1) * page_size
    end = start + page_size
    return {"cdd": mock_data[start:end]}
