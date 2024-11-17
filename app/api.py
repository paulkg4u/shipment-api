from fastapi import FastAPI

app = FastAPI(
    title="Shipment Tracking Service",
    description="This service is used to track shipments",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Shipment Tracking Service"}


@app.get("/shipments")
async def get_shipments():
    return {"message": "Get all shipments"}


@app.get("/shipments/{tracking_number}")
async def get_shipment(tracking_number: str):
    return {"message": f"Get shipment with tracking number {tracking_number}"}
