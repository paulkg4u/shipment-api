import pytest
import json

from app.cache import WeatherCache
from datetime import datetime, timedelta


@pytest.fixture
def weather_cache():
    return WeatherCache()


def test_cache_set_get(weather_cache):
    location = "00000"
    weather_data = {
        "temperature": 289.4,
        "humidity": 44,
        "condition": "few clouds",
        "location": "00000",
        "timestamp": datetime.now().timestamp()
    }

    weather_cache.set(location, weather_data)
    cached_data = weather_cache.get(location)
    assert cached_data["temperature"] == weather_data["temperature"]
    assert cached_data["condition"] == weather_data["condition"]


def test_cache_expiration(weather_cache):
    location = "00000"
    weather_data = {
        "temperature": 289.4,
        "humidity": 44,
        "condition": "few clouds",
        "location": "00000",
        "timestamp": (datetime.now() - timedelta(days=1)).timestamp()
    }

    weather_cache.set(location, weather_data)
    cached_data = weather_cache.get(location)
    assert cached_data is None
