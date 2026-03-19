import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
from fastapi.testclient import TestClient
from backend.main import app

def test_root():
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
