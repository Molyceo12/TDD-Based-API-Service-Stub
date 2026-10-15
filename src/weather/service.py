"""Weather service: checks requests and asks a provider for the forecast."""

from weather.exceptions import CityNotFoundError, InvalidAPIKeyError, InvalidCityError
from weather.models import Forecast, ForecastRequest
from weather.providers import MockWeatherProvider, WeatherProvider

VALID_API_KEYS = frozenset({"demo-key", "test-key"})


class WeatherService:
    """Client for the mock weather API.

    Attributes:
        api_key: Key sent with every request; must be in ``VALID_API_KEYS``.
        provider: Source of forecasts; ``MockWeatherProvider`` by default.
    """

    def __init__(self, api_key: str, provider: WeatherProvider | None = None) -> None:
        self.api_key = api_key
        self.provider = provider or MockWeatherProvider()

    def get_forecast(self, city: str) -> Forecast:
        """Return the forecast for a city.

        Args:
            city: City name; letter case and surrounding spaces are ignored.

        Returns:
            The forecast for the city.

        Raises:
            InvalidAPIKeyError: If the API key is not valid.
            InvalidCityError: If the city name is empty or blank.
            CityNotFoundError: If the provider has no forecast for the city.
        """
        if self.api_key not in VALID_API_KEYS:
            raise InvalidAPIKeyError("Invalid API key")
        name = city.strip()
        if not name:
            raise InvalidCityError("City name must not be empty")
        forecast = self.provider.fetch(ForecastRequest(name))
        if forecast is None:
            raise CityNotFoundError(f"City not found: {city}")
        return forecast
