from client import ApiClient
from config import load_config


def create_client() -> ApiClient:
    config = load_config()
    return ApiClient(config)
