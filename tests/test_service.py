"""Tests for the weather service."""

import pytest

from weather.service import Forecast, WeatherService


def test_get_forecast_returns_london_forecast() -> None:
    service = WeatherService(api_key="demo-key")
    assert service.get_forecast("London") == Forecast("London", 15.0, "Cloudy", 72)


@pytest.mark.parametrize(
    "expected",
    [
        Forecast("London", 15.0, "Cloudy", 72),
        Forecast("Paris", 18.0, "Sunny", 55),
        Forecast("New York", 22.0, "Partly cloudy", 60),
        Forecast("Tokyo", 26.0, "Rainy", 80),
        Forecast("Nairobi", 24.0, "Sunny", 50),
    ],
)
def test_get_forecast_returns_each_known_city(expected: Forecast) -> None:
    service = WeatherService(api_key="demo-key")
    assert service.get_forecast(expected.city) == expected
