"""Mock weather service that returns predefined forecasts."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Forecast:
    """Weather forecast for one city."""

    city: str
    temperature_c: float
    condition: str
    humidity: int


KNOWN_FORECASTS = {
    "London": Forecast("London", 15.0, "Cloudy", 72),
    "Paris": Forecast("Paris", 18.0, "Sunny", 55),
    "New York": Forecast("New York", 22.0, "Partly cloudy", 60),
    "Tokyo": Forecast("Tokyo", 26.0, "Rainy", 80),
    "Nairobi": Forecast("Nairobi", 24.0, "Sunny", 50),
}


class WeatherService:
    """Returns weather forecasts for cities."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city."""
        return KNOWN_FORECASTS[city]
