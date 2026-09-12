from config import load_config


def test_load_config_uses_defaults(monkeypatch):
    monkeypatch.delenv("API_URL", raising=False)
    monkeypatch.delenv("DEBUG", raising=False)
    monkeypatch.delenv("CACHE_TTL_SECONDS", raising=False)

    config = load_config()

    assert config.api_url == "http://localhost:8000"
    assert config.debug is False
    assert config.cache_ttl_seconds == 60


def test_load_config_reads_environment(monkeypatch):
    monkeypatch.setenv("API_URL", "https://api.example.com")
    monkeypatch.setenv("DEBUG", "true")
    monkeypatch.setenv("CACHE_TTL_SECONDS", "120")

    config = load_config()

    assert config.api_url == "https://api.example.com"
    assert config.debug is True
    assert config.cache_ttl_seconds == 120
