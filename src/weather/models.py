"""Data models returned by the weather service."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Forecast:
    """Weather forecast for one city.

    Attributes:
        city: Name of the city, e.g. ``"London"``.
        temperature_c: Temperature in degrees Celsius.
        condition: Short description of the weather, e.g. ``"Sunny"``.
        humidity: Relative humidity as a percentage (0-100).
    """

    city: str
    temperature_c: float
    condition: str
    humidity: int
