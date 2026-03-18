from fastapi import APIRouter, Response, Request

router = APIRouter()

@router.get("/data")
def get_mosaic_data(response: Response, request: Request):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    if "etag" in response.headers:
        del response.headers["etag"]
    # Mocked Mosaic inventory data
    return {
        "mosaic": {
            "sample_id": "SMP456",
            "location": "Freezer A - Rack 3",
            "quantity": 120,
            "unit": "uL",
            "status": "Available"
        }
    }
