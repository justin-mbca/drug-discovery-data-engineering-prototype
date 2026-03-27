import os
from fastapi import APIRouter, Response, Request, Query
# Benchling API credentials (set these as environment variables)
BENCHLING_API_KEY = os.environ.get("BENCHLING_API_KEY")
BENCHLING_BASE_URL = os.environ.get("BENCHLING_BASE_URL", "https://api.benchling.com/v2")
# Switch: use real API if BENCHLING_USE_REAL_API is set to '1', else use mock data
BENCHLING_USE_REAL_API = os.environ.get("BENCHLING_USE_REAL_API", "0") == "1"

router = APIRouter()

@router.get("/data")

@router.get("/data")
def get_benchling_data(response: Response, request: Request, page: int = Query(1, ge=1), page_size: int = Query(100, ge=1, le=1000)):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    if "etag" in response.headers:
        del response.headers["etag"]
    if BENCHLING_USE_REAL_API and BENCHLING_API_KEY:
        import requests
        headers = {"Authorization": f"Bearer {BENCHLING_API_KEY}"}
        try:
            r = requests.get(f"{BENCHLING_BASE_URL}/entities", headers=headers)
            r.raise_for_status()
            data = r.json()
            return {"benchling": data}
        except Exception as e:
            return {"benchling": {"error": str(e)}}
    # Mock data: many records
    mock_data = [
        {"entry_id": f"ELN{790+i}", "experiment": f"Experiment {i}", "date": f"2026-03-{17+i:02d}", "scientist": f"Scientist {i}", "result": f"Result {i}"}
        for i in range(1, 201)
    ]
    # Sort by entry_id to ensure stable order
    mock_data = sorted(mock_data, key=lambda x: x["entry_id"])
    start = (page - 1) * page_size
    end = start + page_size
    return {"benchling": mock_data[start:end]}
