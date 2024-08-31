from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per minute", "20 per second"],
    storage_uri=f"redis://:{os.getenv('REDIS_PASSWORD')}@{os.getenv('REDIS_HOST', 'redis')}:{os.getenv('REDIS_PORT', 6379)}/0"
)
