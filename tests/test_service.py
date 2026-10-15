"""Tests for the weather service."""

from weather.service import Forecast, WeatherService


def test_get_forecast_returns_london_forecast() -> None:
    service = WeatherService(api_key="demo-key")
    assert service.get_forecast("London") == Forecast("London", 15.0, "Cloudy", 72)
