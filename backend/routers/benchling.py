from fastapi import APIRouter

router = APIRouter()

@router.get("/data")
def get_benchling_data():
    # Mocked Benchling ELN data
    return {"benchling": "sample ELN data"}
