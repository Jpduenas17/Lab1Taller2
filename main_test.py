import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/infoUsers/Celia_Harber9')
    assert response.status_code == 200

def test_index_204():
    response = client.get('/infoUsers/Pasquale')
    assert response.status_code == 204