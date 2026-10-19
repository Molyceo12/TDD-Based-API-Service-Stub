"""Weather service, the package entry point: checks requests and asks a provider."""

import logging

from weather.exceptions import (
    CityNotFoundError,
    InvalidAPIKeyError,
    InvalidCityError,
    WeatherServiceError,
)
from weather.models import Forecast, ForecastRequest
from weather.providers import MockWeatherProvider, WeatherProvider
from weather.utils import is_valid_api_key, normalize_city

logger = logging.getLogger(__name__)


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
        name = normalize_city(city)
        logger.info("request city=%s", name)
        try:
            forecast = self._find(name)
        except WeatherServiceError as exc:
            logger.warning("error city=%s reason=%s", name, exc)
            raise
        logger.info(
            "response city=%s condition=%s temperature_c=%s",
            forecast.city,
            forecast.condition,
            forecast.temperature_c,
        )
        return forecast

    def _find(self, name: str) -> Forecast:
        """Check the request and return the provider's forecast."""
        if not is_valid_api_key(self.api_key):
            raise InvalidAPIKeyError("Invalid API key")
        if not name:
            raise InvalidCityError("City name must not be empty")
        forecast = self.provider.fetch(ForecastRequest(name))
        if forecast is None:
            raise CityNotFoundError(f"City not found: {name}")
        return forecast
