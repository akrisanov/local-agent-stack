from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    api_url: str
    debug: bool
    cache_ttl_seconds: int
