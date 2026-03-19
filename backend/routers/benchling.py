import os

# Benchling API credentials (set these as environment variables)
BENCHLING_API_KEY = os.environ.get("BENCHLING_API_KEY")
BENCHLING_BASE_URL = os.environ.get("BENCHLING_BASE_URL", "https://api.benchling.com/v2")
# Switch: use real API if BENCHLING_USE_REAL_API is set to '1', else use mock data
BENCHLING_USE_REAL_API = os.environ.get("BENCHLING_USE_REAL_API", "0") == "1"
from fastapi import APIRouter, Response, Request

router = APIRouter()

@router.get("/data")
def get_benchling_data(response: Response, request: Request):
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
    # Default: return mock data (multiple unique records)
    return {
        "benchling": [
            {
                "entry_id": "ELN789",
                "experiment": "Enzyme Kinetics",
                "date": "2026-03-18",
                "scientist": "Dr. Jane Doe",
                "result": "Increased activity observed at pH 7.4"
            },
            {
                "entry_id": "ELN790",
                "experiment": "Protein Purification",
                "date": "2026-03-17",
                "scientist": "Dr. John Smith",
                "result": "Yield improved with new buffer"
            },
            {
                "entry_id": "ELN791",
                "experiment": "Cell Culture",
                "date": "2026-03-16",
                "scientist": "Dr. Alice Lee",
                "result": "Contamination detected in batch 3"
            }
        ]
    }
