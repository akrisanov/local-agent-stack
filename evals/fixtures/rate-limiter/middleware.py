from limiter import RateLimiter


class RateLimitMiddleware:
    def __init__(self, limiter: RateLimiter):
        self.limiter = limiter

    def handle(self) -> int:
        if not self.limiter.allow():
            return 429

        return 200
