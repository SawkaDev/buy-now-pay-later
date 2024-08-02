from functools import wraps
from .rate_limiting import limiter
from ..services.service_registry import get_service_limits

def apply_rate_limits(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        service = kwargs.get('service')
        limits = get_service_limits(service)
        for limit in limits:
            limiter.limit(limit)(func)
        return func(*args, **kwargs)
    return wrapper
