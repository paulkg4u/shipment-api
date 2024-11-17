from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Shipment Tracking Service"}


def test_get_shipments():
    response = client.get("/shipments")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_shipment():
    response = client.get("/shipments/TN12345680")
    assert response.status_code == 200
    data = response.json()
    assert data["tracking_number"] == "TN12345680"
    assert 'article' in data


def test_get_shipment_not_found():
    response = client.get("/shipments/12345678")
    assert response.status_code == 404
    assert response.json() == {"detail": "Shipment not found"}
