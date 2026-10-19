"""Shared pytest fixtures."""

import pytest

from weather import create_weather_service
from weather.services import WeatherService


@pytest.fixture(name="service")
def fixture_service() -> WeatherService:
    """Return a weather service client with a valid API key."""
    return create_weather_service("demo-key")
