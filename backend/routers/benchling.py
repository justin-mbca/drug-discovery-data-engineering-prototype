from fastapi import APIRouter, Response, Request

router = APIRouter()

@router.get("/data")
def get_benchling_data(response: Response, request: Request):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    if "etag" in response.headers:
        del response.headers["etag"]
    # Mocked Benchling ELN data
    return {
        "benchling": {
            "entry_id": "ELN789",
            "experiment": "Enzyme Kinetics",
            "date": "2026-03-18",
            "scientist": "Dr. Jane Doe",
            "result": "Increased activity observed at pH 7.4"
        }
    }
