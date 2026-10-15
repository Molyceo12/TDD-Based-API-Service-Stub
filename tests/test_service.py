"""Tests for the weather service."""

import pytest

from weather.service import Forecast, WeatherService


@pytest.mark.parametrize(
    "expected",
    [
        Forecast("London", 15.0, "Cloudy", 72),
        Forecast("Paris", 18.0, "Sunny", 55),
        Forecast("New York", 22.0, "Partly cloudy", 60),
        Forecast("Tokyo", 26.0, "Rainy", 80),
        Forecast("Nairobi", 24.0, "Sunny", 50),
    ],
    ids=lambda forecast: forecast.city,
)
def test_get_forecast_returns_each_known_city(
    service: WeatherService, expected: Forecast
) -> None:
    assert service.get_forecast(expected.city) == expected


@pytest.mark.parametrize("city", ["london", "LONDON", "  London  ", " lOnDoN"])
def test_get_forecast_ignores_case_and_spaces(
    service: WeatherService, city: str
) -> None:
    assert service.get_forecast(city) == Forecast("London", 15.0, "Cloudy", 72)
