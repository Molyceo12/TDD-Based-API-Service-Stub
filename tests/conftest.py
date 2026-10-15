"""Shared pytest fixtures."""

import pytest

from weather.service import WeatherService


@pytest.fixture(name="service")
def fixture_service() -> WeatherService:
    """Return a weather service client with a valid API key."""
    return WeatherService(api_key="demo-key")
