"""Tests for the weather service factory."""

from pytest_mock import MockerFixture

from weather import create_weather_service
from weather.providers import MockWeatherProvider, WeatherProvider


def test_factory_uses_mock_provider_by_default() -> None:
    service = create_weather_service("demo-key")
    assert isinstance(service.provider, MockWeatherProvider)


def test_factory_uses_given_provider(mocker: MockerFixture) -> None:
    provider = mocker.create_autospec(WeatherProvider, instance=True)
    assert create_weather_service("demo-key", provider).provider is provider
