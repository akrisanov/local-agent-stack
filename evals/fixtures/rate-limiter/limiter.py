class RateLimiter:
    def __init__(self, max_requests: int):
        self.max_requests = max_requests
        self._requests = 0

    def allow(self) -> bool:
        if self._requests >= self.max_requests:
            return False

        self._requests += 1
        return True
