from cache import Cache


def test_cache_returns_stored_value():
    cache = Cache(ttl_seconds=60)

    cache.set("user:1", {"name": "Alice"})

    assert cache.get("user:1") == {"name": "Alice"}


def test_cache_returns_none_for_missing_key():
    cache = Cache(ttl_seconds=60)

    assert cache.get("missing") is None
