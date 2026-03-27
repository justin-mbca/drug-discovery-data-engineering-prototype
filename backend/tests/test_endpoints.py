
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

@pytest.mark.parametrize("endpoint, key", [
    ("/benchling/data", "benchling"),
    ("/cdd/data", "cdd"),
    ("/mosaic/data", "mosaic"),
])
def test_mock_api_batch(endpoint, key):
    # Test page 1 and page 2 with same page_size
    page_size = 10
    resp1 = client.get(f"{endpoint}?page=1&page_size={page_size}")
    assert resp1.status_code == 200
    data1 = resp1.json()
    assert key in data1
    assert isinstance(data1[key], list)
    assert len(data1[key]) == page_size
    resp2 = client.get(f"{endpoint}?page=2&page_size={page_size}")
    assert resp2.status_code == 200
    data2 = resp2.json()
    assert key in data2
    assert isinstance(data2[key], list)
    assert len(data2[key]) == page_size
    # Ensure no overlap between page 1 and page 2
    ids1 = {str(item) for item in data1[key]}
    ids2 = {str(item) for item in data2[key]}
    assert ids1.isdisjoint(ids2)
