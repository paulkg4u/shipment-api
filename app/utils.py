import requests
import json
import csv

from app.schema import Shipment, Article
class ShipmentService:

    def __init__(self):
        self.csv_file = "data/shipments.csv"
        self.shipments = []

    async def load_shipments(self):
        with open(self.csv_file) as f:
            self.shipments = list(csv.DictReader(f))

    async def get_all_shipments(self) -> list[Shipment]:

        await self.load_shipments()
        return [await self.create_shipment_object(shipment) for shipment in self.shipments]

    async def get_shipment(self, tracking_number: str) -> Shipment:

        with open(self.csv_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["tracking_number"] == tracking_number:
                    return await self.create_shipment_object(row)
        return None

    async def create_shipment_object(self, shipment_data: dict) -> Shipment:

        article = Article(
            name=shipment_data["article_name"],
            price=shipment_data["article_price"],
            SKU=shipment_data["SKU"]
        )

        return Shipment(
            tracking_number=shipment_data["tracking_number"],
            carrier=shipment_data["carrier"],
            sender_adderss=shipment_data["sender_address"],
            receiver_address=shipment_data["receiver_address"],
            status=shipment_data["status"],
            quantity=shipment_data["article_quantity"],
            article=article,
            weather=None
        )
