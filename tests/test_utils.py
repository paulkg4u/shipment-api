import pytest
from app.utils import ShipmentService, WeatherService
from app.schema import Shipment, Weather


@pytest.fixture
def weather_service():
    return WeatherService()


@pytest.fixture
def shipment_service():
    return ShipmentService()


@pytest.mark.asyncio
async def test_get_all_shipments(shipment_service):
    shipments = await shipment_service.get_all_shipments()
    assert len(shipments) > 0


@pytest.mark.asyncio
async def test_get_shipment(shipment_service):
    shipment = await shipment_service.get_shipment("TN12345678")
    assert isinstance(shipment, Shipment)
    assert shipment.tracking_number == "TN12345678"


@pytest.mark.asyncio
async def test_get_weather(weather_service):
    weather = await weather_service.get_weather("28013")
    assert isinstance(weather, Weather)
