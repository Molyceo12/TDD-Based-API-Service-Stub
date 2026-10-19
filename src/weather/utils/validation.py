"""Request checks shared by the weather service."""

VALID_API_KEYS = frozenset({"demo-key", "test-key"})


def is_valid_api_key(api_key: str) -> bool:
    """Check whether an API key is accepted by the service.

    Args:
        api_key: Key sent with the request.

    Returns:
        ``True`` if the key is in ``VALID_API_KEYS``.
    """
    return api_key in VALID_API_KEYS


def normalize_city(city: str) -> str:
    """Clean up a city name before it is used.

    Args:
        city: City name as typed by the caller.

    Returns:
        The name without surrounding spaces (may be empty).
    """
    return city.strip()
