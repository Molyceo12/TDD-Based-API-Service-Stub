"""Tests for the mock weather provider."""

import pytest

from weather.models import Forecast, ForecastRequest
from weather.providers import MockWeatherProvider


@pytest.mark.parametrize(
    ("city", "expected"),
    [
        ("London", Forecast("London", 15.0, "Cloudy", 72)),
        ("paris", Forecast("Paris", 18.0, "Sunny", 55)),
        ("NEW YORK", Forecast("New York", 22.0, "Partly cloudy", 60)),
        ("Tokyo", Forecast("Tokyo", 26.0, "Rainy", 80)),
        ("Nairobi", Forecast("Nairobi", 24.0, "Sunny", 50)),
        ("Atlantis", None),
    ],
)
def test_mock_provider_returns_known_cities_or_none(
    city: str, expected: Forecast | None
) -> None:
    assert MockWeatherProvider().fetch(ForecastRequest(city)) == expected
