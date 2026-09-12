import time
from typing import Any


class Cache:
    def __init__(self, ttl_seconds: int):
        self.ttl_seconds = ttl_seconds
        self._items: dict[str, tuple[Any, float]] = {}

    def set(self, key: str, value: Any) -> None:
        self._items[key] = (value, time.monotonic())

    def get(self, key: str) -> Any | None:
        item = self._items.get(key)
        if item is None:
            return None

        value, created_at = item

        if time.monotonic() - created_at >= self.ttl_seconds:
            del self._items[key]
            return None

        return value
