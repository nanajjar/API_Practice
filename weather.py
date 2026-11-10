"""Functions for retrieving current weather from Open-Meteo Forecast."""

from api_client import get_json

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(latitude, longitude):
    """Return (temperature_celsius, wind_speed_kmh) for the location."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    }

    # TODO: Call get_json(FORECAST_URL, params).
    # TODO: Access the nested "current" dictionary.
    # TODO: Retrieve "temperature_2m" and "wind_speed_10m".
    # TODO: Return both values as a tuple.
    raise NotImplementedError("Complete get_weather() in weather.py")
