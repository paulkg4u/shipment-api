from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Article(BaseModel):
    name: str
    price: float
    SKU: str


class Weather(BaseModel):
    temperature: float
    humidity: float
    condition: str
    location: str
    timestamp: float


class Shipment(BaseModel):
    tracking_number: str
    carrier: str
    sender_adderss: str
    receiver_address: str
    status: str
    quantity: int
    article: Article
    weather: Optional[Weather]
