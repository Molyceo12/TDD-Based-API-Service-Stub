"""Mock weather service that returns predefined forecasts."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Forecast:
    """Weather forecast for one city."""

    city: str
    temperature_c: float
    condition: str
    humidity: int


class WeatherService:
    """Returns weather forecasts for cities."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city."""
        return Forecast(city, 15.0, "Cloudy", 72)
