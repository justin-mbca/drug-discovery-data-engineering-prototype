from fastapi import APIRouter

router = APIRouter()

@router.get("/data")
def get_mosaic_data():
    # Mocked Mosaic inventory data
    return {"mosaic": "sample inventory data"}
