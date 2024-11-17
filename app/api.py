import logging
from fastapi import FastAPI, HTTPException
from typing import List

from app.schema import Shipment
from app.utils import ShipmentService

# Create a logger
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Shipment Tracking Service",
    description="This service is used to track shipments",
    version="1.0.0"
)


@app.get("/")
async def root():
    logger.info("Received request to root endpoint")
    return {"message": "Welcome to the Shipment Tracking Service"}


@app.get(
    path="/shipments",
    response_model=List[Shipment],
    summary="Get all shipments",
    description="Get all shipments"
)
async def get_shipments():
    logger.info("Received request to get all shipments")
    shipments = await ShipmentService().get_all_shipments()
    logger.info("Successfully retrieved all shipments")
    return shipments

@app.get("/shipments/{tracking_number}")
async def get_shipment(tracking_number: str):
    logger.info(f"Received request to get shipment with tracking number {
                tracking_number}")
    shipment = await ShipmentService().get_shipment(tracking_number)
    if shipment is None:
        logger.error(f"Shipment with tracking number {
                     tracking_number} not found")
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment
