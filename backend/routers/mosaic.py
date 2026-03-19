import os

# Mosaic API credentials (set these as environment variables)
MOSAIC_API_KEY = os.environ.get("MOSAIC_API_KEY")
MOSAIC_BASE_URL = os.environ.get("MOSAIC_BASE_URL", "https://api.mosaic.com/v1")
from fastapi import APIRouter, Response, Request

router = APIRouter()

@router.get("/data")
def get_mosaic_data(response: Response, request: Request):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    if "etag" in response.headers:
        del response.headers["etag"]
    # Mocked Mosaic inventory data (multiple unique records)
    return {
        "mosaic": [
            {
                "sample_id": "SMP456",
                "location": "Freezer A - Rack 3",
                "quantity": 120,
                "unit": "uL",
                "status": "Available"
            },
            {
                "sample_id": "SMP457",
                "location": "Freezer B - Rack 1",
                "quantity": 80,
                "unit": "uL",
                "status": "Checked Out"
            },
            {
                "sample_id": "SMP458",
                "location": "Refrigerator - Shelf 2",
                "quantity": 200,
                "unit": "uL",
                "status": "Available"
            }
        ]
    }
