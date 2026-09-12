from typing import Any

from cache import Cache
from models import AppConfig


class ApiClient:
    def __init__(self, config: AppConfig):
        self.config = config
        self.cache = Cache(config.cache_ttl_seconds)

    def build_headers(self) -> dict[str, str]:
        headers = {
            "Accept": "application/json",
        }

        if self.config.debug:
            headers["X-Debug"] = "true"

        return headers

    def cache_response(self, key: str, response: Any) -> None:
        self.cache.set(key, response)

    def get_cached_response(self, key: str) -> Any | None:
        return self.cache.get(key)
