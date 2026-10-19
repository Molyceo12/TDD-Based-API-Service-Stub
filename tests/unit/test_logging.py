"""Tests for the service's structured logging."""

import logging

import pytest

from weather.exceptions import CityNotFoundError
from weather.services import WeatherService


def test_logs_request_and_response(
    service: WeatherService, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.INFO, logger="weather.services.weather_service")
    service.get_forecast(" London ")
    assert caplog.messages == [
        "request city=London",
        "response city=London condition=Cloudy temperature_c=15.0",
    ]


def test_logs_errors_as_warnings(
    service: WeatherService, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.INFO, logger="weather.services.weather_service")
    with pytest.raises(CityNotFoundError):
        service.get_forecast("Atlantis")
    assert caplog.records[-1].levelname == "WARNING"
    assert caplog.messages[-1] == "error city=Atlantis reason=City not found: Atlantis"
