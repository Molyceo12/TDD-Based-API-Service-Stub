"""Mock weather service that returns predefined forecasts."""

from weather.exceptions import CityNotFoundError, InvalidAPIKeyError, InvalidCityError
from weather.models import Forecast
from weather.providers import WeatherProvider

# Keys are lowercase so lookups can ignore the letter case of the input.
KNOWN_FORECASTS: dict[str, Forecast] = {
    "london": Forecast("London", 15.0, "Cloudy", 72),
    "paris": Forecast("Paris", 18.0, "Sunny", 55),
    "new york": Forecast("New York", 22.0, "Partly cloudy", 60),
    "tokyo": Forecast("Tokyo", 26.0, "Rainy", 80),
    "nairobi": Forecast("Nairobi", 24.0, "Sunny", 50),
}

VALID_API_KEYS = frozenset({"demo-key", "test-key"})


class WeatherService:
    """Client for the mock weather API.

    Attributes:
        api_key: Key sent with every request; must be in ``VALID_API_KEYS``.
    """

    def __init__(self, api_key: str, provider: WeatherProvider | None = None) -> None:
        self.api_key = api_key
        self.provider = provider

    def get_forecast(self, city: str) -> Forecast:
        """Return the predefined forecast for a city.

        Args:
            city: City name; letter case and surrounding spaces are ignored.

        Returns:
            The forecast for the city.

        Raises:
            InvalidAPIKeyError: If the API key is not valid.
            InvalidCityError: If the city name is empty or blank.
            CityNotFoundError: If the city is not a known city.
        """
        if self.api_key not in VALID_API_KEYS:
            raise InvalidAPIKeyError("Invalid API key")
        name = city.strip()
        if not name:
            raise InvalidCityError("City name must not be empty")
        forecast = KNOWN_FORECASTS.get(name.lower())
        if forecast is None:
            raise CityNotFoundError(f"City not found: {city}")
        return forecast
