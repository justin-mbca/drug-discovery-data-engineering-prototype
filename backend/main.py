
from fastapi import FastAPI
from routers import cdd, mosaic, benchling
from utils.bigquery_client import get_bigquery_data


app = FastAPI()


app.include_router(cdd.router, prefix="/cdd")
app.include_router(mosaic.router, prefix="/mosaic")
app.include_router(benchling.router, prefix="/benchling")


@app.get("/")
def read_root():
    return {"message": "Drug Discovery Data Engineering Prototype"}


# New endpoint for BigQuery data
@app.get("/bigquery/data")
def bigquery_data():
    return get_bigquery_data()
