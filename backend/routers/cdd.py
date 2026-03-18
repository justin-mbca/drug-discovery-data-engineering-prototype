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
    # Mocked CDD Vault data
    return {
        "cdd": {
            "compound_id": "ABC123",
            "name": "Aspirin",
            "structure": "CC(=O)OC1=CC=CC=C1C(=O)O",
            "activity": "Active",
            "project": "Pain Relief"
        }
    }
