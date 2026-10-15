"""Tests for the weather service."""

import pytest
from pytest_mock import MockerFixture

from weather.exceptions import (
    CityNotFoundError,
    InvalidAPIKeyError,
    InvalidCityError,
    WeatherServiceError,
)
from weather.models import Forecast, ForecastRequest
from weather.providers import WeatherProvider
from weather.service import WeatherService

ATLANTIS = Forecast("Atlantis", 30.0, "Stormy", 99)


def test_get_forecast_uses_injected_provider(mocker: MockerFixture) -> None:
    provider = mocker.create_autospec(WeatherProvider, instance=True)
    provider.fetch.return_value = ATLANTIS
    assert WeatherService("demo-key", provider).get_forecast(" Atlantis ") == ATLANTIS
    provider.fetch.assert_called_once_with(ForecastRequest("Atlantis"))


def test_get_forecast_raises_when_provider_has_no_data(mocker: MockerFixture) -> None:
    provider = mocker.create_autospec(WeatherProvider, instance=True)
    provider.fetch.return_value = None
    with pytest.raises(CityNotFoundError):
        WeatherService("demo-key", provider).get_forecast("London")


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


@pytest.mark.parametrize("city", ["Atlantis", "Gotham", "Londonn"])
def test_get_forecast_unknown_city_raises_city_not_found(
    service: WeatherService, city: str
) -> None:
    with pytest.raises(CityNotFoundError, match=city):
        service.get_forecast(city)


@pytest.mark.parametrize("api_key", ["wrong-key", "", "DEMO-KEY"])
def test_get_forecast_invalid_api_key_raises(api_key: str) -> None:
    with pytest.raises(InvalidAPIKeyError):
        WeatherService(api_key=api_key).get_forecast("London")


@pytest.mark.parametrize("city", ["", "   ", "\t\n"])
def test_get_forecast_empty_city_raises_invalid_city(
    service: WeatherService, city: str
) -> None:
    with pytest.raises(InvalidCityError):
        service.get_forecast(city)


@pytest.mark.parametrize(
    ("api_key", "city"), [("demo-key", "Atlantis"), ("bad", "London"), ("demo-key", "")]
)
def test_all_errors_are_weather_service_errors(api_key: str, city: str) -> None:
    with pytest.raises(WeatherServiceError):
        WeatherService(api_key=api_key).get_forecast(city)


def test_get_forecast_reads_from_forecast_table(
    service: WeatherService, mocker: MockerFixture
) -> None:
    fake = Forecast("Atlantis", 30.0, "Stormy", 99)
    mocker.patch.dict("weather.service.KNOWN_FORECASTS", {"atlantis": fake})
    assert service.get_forecast("Atlantis") == fake
