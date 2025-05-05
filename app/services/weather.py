import requests
from app.core.config import settings
from app.services.cache import cache_service

class WeatherService:
    def __init__(self):
        self.base_url = settings.WEATHER_API_URL
        self.api_key = settings.API_KEY

    def get_weather(self, location: str, days: int = 1):
        # Try to get from cache first
        cached_data = cache_service.get(location)
        if cached_data:
            return cached_data

        # If not in cache, call the API
        url = f"{self.base_url}/{location}/next{days}days"
        params = {
            "unitGroup": "metric",
            "key": self.api_key,
            "include": "days",
            "contentType": "json"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Store in cache
        cache_service.set(location, data)

        return data

weather_service = WeatherService()