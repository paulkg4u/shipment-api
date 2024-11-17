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
    assert response.json() == {"message": "Get all shipments"}


def test_get_shipment():
    response = client.get("/shipments/TN12345680")
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Get shipment with tracking number TN12345680"}
