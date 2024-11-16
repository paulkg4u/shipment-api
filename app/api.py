from fastapi import FastAPI

app = FastAPI(
    title="Shipment Tracking Service",
    description="This service is used to track shipments",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Shipment Tracking Service"}
