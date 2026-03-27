import os
from fastapi import APIRouter, Response, Request, Query
# Mosaic API credentials (set these as environment variables)
MOSAIC_API_KEY = os.environ.get("MOSAIC_API_KEY")
MOSAIC_BASE_URL = os.environ.get("MOSAIC_BASE_URL", "https://api.mosaic.com/v1")

router = APIRouter()

@router.get("/data")

@router.get("/data")
def get_mosaic_data(response: Response, request: Request, page: int = Query(1, ge=1), page_size: int = Query(100, ge=1, le=1000)):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    if "etag" in response.headers:
        del response.headers["etag"]
    # Mock data: many records
    mock_data = [
        {"sample_id": f"SMP{i:04d}", "location": f"Location {i%10}", "quantity": 100+i, "unit": "uL", "status": "Available" if i%2==0 else "Checked Out"}
        for i in range(1, 201)
    ]
    # Sort by sample_id to ensure stable order
    mock_data = sorted(mock_data, key=lambda x: x["sample_id"])
    start = (page - 1) * page_size
    end = start + page_size
    return {"mosaic": mock_data[start:end]}
