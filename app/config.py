from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Shipment Tracking Service"
    version: str = "1.0.0"
    OPEN_WEATHER_API_KEY: str
    REDIS_HOST: str
    redis_port: int = 6379
    weather_cache_ttl: int = 7200
    CSV_FILE_PATH: str

    model_config = SettingsConfigDict(env_file=".env")



@lru_cache
def get_settings():
    return Settings()
