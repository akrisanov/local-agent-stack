from unittest.mock import patch

from cache import Cache


def test_returns_value_before_ttl_expires():
    cache = Cache(ttl_seconds=10)

    with patch("cache.time.monotonic", side_effect=[100.0, 105.0]):
        cache.put("key", "value")
        assert cache.get("key") == "value"


def test_returns_none_after_ttl_expires():
    cache = Cache(ttl_seconds=10)

    with patch("cache.time.monotonic", side_effect=[100.0, 111.0]):
        cache.put("key", "value")
        assert cache.get("key") is None


def test_returns_none_when_ttl_exactly_expires():
    cache = Cache(ttl_seconds=10)

    with patch("cache.time.monotonic", side_effect=[100.0, 110.0]):
        cache.put("key", "value")
        assert cache.get("key") is None
