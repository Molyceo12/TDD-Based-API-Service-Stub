"""Mock weather service that returns predefined forecasts."""

from dataclasses import dataclass


class WeatherServiceError(Exception):
    """Base class for all weather service errors."""


class CityNotFoundError(Exception):
    """The city is not one of the known cities."""


class InvalidAPIKeyError(Exception):
    """The API key is missing or not valid."""


class InvalidCityError(Exception):
    """The city name is empty or blank."""


@dataclass(frozen=True)
class Forecast:
    """Weather forecast for one city."""

    city: str
    temperature_c: float
    condition: str
    humidity: int


# Keys are lowercase so lookups can ignore the letter case of the input.
KNOWN_FORECASTS = {
    "london": Forecast("London", 15.0, "Cloudy", 72),
    "paris": Forecast("Paris", 18.0, "Sunny", 55),
    "new york": Forecast("New York", 22.0, "Partly cloudy", 60),
    "tokyo": Forecast("Tokyo", 26.0, "Rainy", 80),
    "nairobi": Forecast("Nairobi", 24.0, "Sunny", 50),
}


VALID_API_KEYS = frozenset({"demo-key", "test-key"})


class WeatherService:
    """Returns weather forecasts for cities."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city."""
        if self.api_key not in VALID_API_KEYS:
            raise InvalidAPIKeyError("Invalid API key")
        if not city.strip():
            raise InvalidCityError("City name must not be empty")
        forecast = KNOWN_FORECASTS.get(city.strip().lower())
        if forecast is None:
            raise CityNotFoundError(f"City not found: {city}")
        return forecast
