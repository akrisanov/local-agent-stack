from app import create_client


def test_debug_header_is_enabled(monkeypatch):
    monkeypatch.setenv("DEBUG", "true")

    client = create_client()

    assert client.build_headers()["X-Debug"] == "true"


def test_debug_header_is_disabled(monkeypatch):
    monkeypatch.setenv("DEBUG", "false")

    client = create_client()

    assert "X-Debug" not in client.build_headers()
