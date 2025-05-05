from pydantic import BaseModel
from typing import Optional, List

class WeatherDay(BaseModel):
    datetime: str
    tempmax: float
    tempmin: float
    temp: float
    conditions: str
    description: str

class WeatherResponse(BaseModel):
    address: str
    days: List[WeatherDay]