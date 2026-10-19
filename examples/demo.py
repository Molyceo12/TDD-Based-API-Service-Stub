"""Send a few sample requests to the weather service and print the results as a table.

Usage:
    python -m poetry run python examples/demo.py
"""

import logging

from weather import create_weather_service
from weather.exceptions import WeatherServiceError

# (api_key, city): successes first, then at least one case per error.
CASES = [
    ("demo-key", "London"),
    ("demo-key", "  nEw YoRk "),
    ("test-key", "Tokyo"),
    ("demo-key", "Atlantis"),
    ("demo-key", "Londonn"),
    ("demo-key", ""),
    ("demo-key", "   "),
    ("wrong-key", "London"),
    ("DEMO-KEY", "Paris"),
]


def run(api_key: str, city: str) -> str:
    """Return the forecast, or the error name and message, as one line of text."""
    try:
        forecast = create_weather_service(api_key).get_forecast(city)
    except WeatherServiceError as exc:
        return f"{type(exc).__name__}: {exc}"
    return (
        f"{forecast.city}, {forecast.temperature_c} C, "
        f"{forecast.condition}, {forecast.humidity}%"
    )


def main() -> None:
    """Run every case and print one table row per case."""
    logging.disable()  # hide the service's log lines; show only the table
    rows = [[repr(key), repr(city), run(key, city)] for key, city in CASES]
    headers = ["API key", "City", "Result"]
    columns = zip(headers, *rows, strict=True)
    widths = [max(len(cell) for cell in column) for column in columns]
    border = "+" + "+".join("-" * (width + 2) for width in widths) + "+"

    print(border)
    for row in [headers, *rows]:
        cells = (cell.ljust(width) for cell, width in zip(row, widths, strict=True))
        print("| " + " | ".join(cells) + " |")
        if row is headers:
            print(border)
    print(border)


if __name__ == "__main__":
    main()
