from limiter import RateLimiter
from middleware import RateLimitMiddleware


def test_middleware_returns_200_for_allowed_request():
    middleware = RateLimitMiddleware(RateLimiter(max_requests=1))

    assert middleware.handle() == 200


def test_middleware_returns_429_when_limit_is_exceeded():
    middleware = RateLimitMiddleware(RateLimiter(max_requests=1))

    assert middleware.handle() == 200
    assert middleware.handle() == 429
