from limiter import RateLimiter


def test_allows_requests_within_limit():
    limiter = RateLimiter(max_requests=2)

    assert limiter.allow() is True
    assert limiter.allow() is True


def test_rejects_requests_above_limit():
    limiter = RateLimiter(max_requests=2)

    assert limiter.allow() is True
    assert limiter.allow() is True
    assert limiter.allow() is False
