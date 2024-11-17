import redis
import json

from datetime import datetime

from app.config import get_settings


class WeatherCache:
    def __init__(self):
        self.settings = get_settings()
        self.redis = redis.Redis(
            host=self.settings.redis_host,
            port=self.settings.redis_port,
            decode_responses=True
        )

    def get(self, location: str) -> dict:
        """
        Get weather data from cache
        """
        data = self.redis.get(location)
        if data:
            weather_data = json.loads(data)
            timestamp = datetime.fromtimestamp(weather_data['timestamp'])
            if (datetime.now() - timestamp).total_seconds() < self.settings.weather_cache_ttl:
                return weather_data

        return None

    def set(self, location: str, data: dict):
        """
        Set weather data in cache
        """
        self.redis.set(
            location,
            json.dumps(data),
            ex=self.settings.weather_cache_ttl
        )
