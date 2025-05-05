from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, RedisDsn

class Settings(BaseSettings):
    API_KEY: str
    WEATHER_API_URL: AnyHttpUrl = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USERNAME: str
    REDIS_PASSWORD: str
    CACHE_EXPIRE_SECONDS: int = 43200  # 12 hours

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_USERNAME}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()