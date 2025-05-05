from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from app.services.weather import WeatherService
from app.schemas.schemas import WeatherResponse
from app.core.dependencies import get_weather_service

app = FastAPI(title="Weather API Wrapper Service")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather/{location}", response_model=WeatherResponse)
async def get_weather(
    location: str,
    days: int = 1,
    weather_service: WeatherService = Depends(get_weather_service)
):
    try:
        weather_data = weather_service.get_weather(location, days)
        return weather_data
    except requests.exceptions.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail="Failed to fetch weather data"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}