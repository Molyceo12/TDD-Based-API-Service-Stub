"""Custom exceptions raised by the weather service."""


class WeatherServiceError(Exception):
    """Base class for all weather service errors.

    Catch this to handle every expected service error in one place.
    """


class CityNotFoundError(WeatherServiceError):
    """Raised when the requested city is not one of the known cities."""


class InvalidAPIKeyError(WeatherServiceError):
    """Raised when the API key is missing or not valid."""


class InvalidCityError(WeatherServiceError):
    """Raised when the city name is empty or only whitespace."""
