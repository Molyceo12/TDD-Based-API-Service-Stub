"""Weather providers: the provider interface and its implementations."""

from weather.providers.base import WeatherProvider
from weather.providers.mock_provider import KNOWN_FORECASTS, MockWeatherProvider

__all__ = ["KNOWN_FORECASTS", "MockWeatherProvider", "WeatherProvider"]
