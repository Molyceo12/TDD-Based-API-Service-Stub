"""Tests for the request checks in ``weather.utils``."""

import pytest

from weather.utils import is_valid_api_key, normalize_city


@pytest.mark.parametrize(("api_key", "expected"), [("demo-key", True), ("bad", False)])
def test_is_valid_api_key(api_key: str, expected: bool) -> None:
    assert is_valid_api_key(api_key) is expected


@pytest.mark.parametrize(
    ("city", "expected"), [("  London ", "London"), ("Paris", "Paris"), ("   ", "")]
)
def test_normalize_city_strips_spaces(city: str, expected: str) -> None:
    assert normalize_city(city) == expected
