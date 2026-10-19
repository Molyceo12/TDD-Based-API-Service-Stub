"""Builds a ready-to-use weather service (the only place that picks a provider)."""

from weather.providers import MockWeatherProvider, WeatherProvider
from weather.services import WeatherService


def create_weather_service(
    api_key: str, provider: WeatherProvider | None = None
) -> WeatherService:
    """Return a weather service that uses the given provider.

    Args:
        api_key: Key sent with every request.
        provider: Source of forecasts; ``MockWeatherProvider`` if not given.

    Returns:
        A ``WeatherService`` wired to the provider.
    """
    return WeatherService(api_key, provider or MockWeatherProvider())
