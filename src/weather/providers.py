"""Weather providers: where the forecast data comes from."""

from abc import ABC, abstractmethod

from weather.models import Forecast, ForecastRequest


class WeatherProvider(ABC):
    """Interface for any source of weather forecasts."""

    @abstractmethod
    def fetch(self, request: ForecastRequest) -> Forecast | None:
        """Return the forecast for the requested city, or ``None`` if unknown."""
