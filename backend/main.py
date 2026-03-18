
from fastapi import FastAPI
from routers import cdd, mosaic, benchling
from routers import mock_etl
from utils.bigquery_client import get_bigquery_data



from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(cdd.router, prefix="/cdd")
app.include_router(mosaic.router, prefix="/mosaic")
app.include_router(benchling.router, prefix="/benchling")
app.include_router(mock_etl.router, prefix="/mock")


@app.get("/")
def read_root():
    return {"message": "Drug Discovery Data Engineering Prototype"}


# New endpoint for BigQuery data
@app.get("/bigquery/data")
def bigquery_data():
    return get_bigquery_data()
