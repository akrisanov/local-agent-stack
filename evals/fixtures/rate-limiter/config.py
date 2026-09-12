from dataclasses import dataclass


@dataclass(frozen=True)
class RateLimitConfig:
    max_requests: int = 3
