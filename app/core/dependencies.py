from fastapi import Depends, HTTPException, status
from app.services.weather import weather_service

def get_weather_service():
    return weather_service