from fastapi import FastAPI, HTTPException
from typing import List

from app.schema import Shipment
from app.utils import ShipmentService

app = FastAPI(
    title="Shipment Tracking Service",
    description="This service is used to track shipments",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Shipment Tracking Service"}


@app.get(
    path="/shipments",
    response_model=List[Shipment],
    summary="Get all shipments",
    description="Get all shipments"
)
async def get_shipments():
    shipments = await ShipmentService().get_all_shipments()
    return shipments

@app.get("/shipments/{tracking_number}")
async def get_shipment(tracking_number: str):
    shipment = await ShipmentService().get_shipment(tracking_number)
    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment
