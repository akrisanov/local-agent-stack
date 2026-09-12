import os

from models import AppConfig


def load_config() -> AppConfig:
    return AppConfig(
        api_url=os.getenv("API_URL", "http://localhost:8000"),
        debug=bool(os.getenv("DEBUG", "")),
        cache_ttl_seconds=int(os.getenv("CACHE_TTL_SECONDS", "60")),
    )
