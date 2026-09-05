import time


class Cache:
    def __init__(self, ttl_seconds: float):
        self.ttl_seconds = ttl_seconds
        self._items = {}

    def put(self, key: str, value: str) -> None:
        self._items[key] = (value, time.monotonic())

    def get(self, key: str) -> str | None:
        item = self._items.get(key)
        if item is None:
            return None

        value, created_at = item

        if time.monotonic() - created_at < self.ttl_seconds:
            del self._items[key]
            return None

        return value
