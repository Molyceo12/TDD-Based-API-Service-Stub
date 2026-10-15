"""Weather providers: where the forecast data comes from."""

from abc import ABC, abstractmethod

from weather.models import Forecast, ForecastRequest


class WeatherProvider(ABC):
    """Interface for any source of weather forecasts."""

    @abstractmethod
    def fetch(self, request: ForecastRequest) -> Forecast | None:
        """Return the forecast for the requested city, or ``None`` if unknown."""


class MockWeatherProvider(WeatherProvider):
    """Provider that returns predefined forecasts instead of calling a real API."""

    def fetch(self, request: ForecastRequest) -> Forecast | None:
        """Return the predefined forecast for the city, or ``None`` if unknown."""
        raise NotImplementedError(request.city)
