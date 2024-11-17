import requests
import json
import csv
from datetime import datetime

from app.schema import Shipment, Article, Weather
from app.config import get_settings
from app.cache import WeatherCache

class ShipmentService:

    def __init__(self):
        self.weather_service = WeatherService()
        self.csv_file = "data/shipments.csv"
        self.shipments = []

    async def load_shipments(self):
        """
        Load shipments from csv file
        """
        with open(self.csv_file) as f:
            self.shipments = list(csv.DictReader(f))

    async def get_all_shipments(self) -> list[Shipment]:
        """
        Get all shipments
        """
        await self.load_shipments()
        return [await self.create_shipment_object(shipment) for shipment in self.shipments] or []

    async def get_shipment(self, tracking_number: str) -> Shipment:
        """
        Get a shipment by tracking number
        """
        with open(self.csv_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["tracking_number"] == tracking_number:
                    return await self.create_shipment_object(row)
        return None

    async def create_shipment_object(self, shipment_data: dict) -> Shipment:
        """
        Create a Shipment object from a dictionary
        """

        article = Article(
            name=shipment_data["article_name"],
            price=shipment_data["article_price"],
            SKU=shipment_data["SKU"]
        )

        weather = await self.weather_service.get_weather(shipment_data['receiver_address'].split(",")[1].strip().split(" ")[0])
        return Shipment(
            tracking_number=shipment_data["tracking_number"],
            carrier=shipment_data["carrier"],
            sender_adderss=shipment_data["sender_address"],
            receiver_address=shipment_data["receiver_address"],
            status=shipment_data["status"],
            quantity=shipment_data["article_quantity"],
            article=article,
            weather=weather
        )


class WeatherService:
    def __init__(self):
        self.settings = get_settings()
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.cache = WeatherCache()

    async def get_weather(self, location: str) -> Weather:
        if weather := self.cache.get(location):
            return Weather(**weather)
        try:
            response = requests.get(f"{self.base_url}?q={location}&appid={
                                    self.settings.OPEN_WEATHER_API_KEY}")
            if response.status_code == 200:
                data = response.json()
                weather = Weather(
                    temperature=data["main"]["temp"],
                    humidity=data["main"]["humidity"],
                    condition=f"{data["weather"][0]["description"]}",
                    location=data["name"],
                    timestamp=datetime.now().timestamp()
                )
                self.cache.set(location, weather.model_dump())

                return weather
            else:
                return None
        except:
            return None
