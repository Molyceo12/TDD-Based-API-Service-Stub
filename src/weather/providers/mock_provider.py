"""Mock weather provider with predefined forecasts."""

from weather.models import Forecast, ForecastRequest
from weather.providers.base import WeatherProvider

# Keys are lowercase so lookups can ignore the letter case of the input.
KNOWN_FORECASTS: dict[str, Forecast] = {
    "london": Forecast("London", 15.0, "Cloudy", 72),
    "paris": Forecast("Paris", 18.0, "Sunny", 55),
    "new york": Forecast("New York", 22.0, "Partly cloudy", 60),
    "tokyo": Forecast("Tokyo", 26.0, "Rainy", 80),
    "nairobi": Forecast("Nairobi", 24.0, "Sunny", 50),
}


class MockWeatherProvider(WeatherProvider):
    """Provider that returns predefined forecasts instead of calling a real API."""

    def fetch(self, request: ForecastRequest) -> Forecast | None:
        """Return the predefined forecast for the city, or ``None`` if unknown."""
        return KNOWN_FORECASTS.get(request.city.lower())
