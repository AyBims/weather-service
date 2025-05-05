import json
from redis import Redis
from redis.exceptions import RedisError
from app.core.config import settings

class CacheService:
    def __init__(self):
        self.redis = Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            username=settings.REDIS_USERNAME,
            password=settings.REDIS_PASSWORD,
            decode_responses=False,  # Keep as False since we're handling JSON serialization
            socket_timeout=5,  # Add timeout
            socket_connect_timeout=5  # Add connection timeout
        )
        self.expire = settings.CACHE_EXPIRE_SECONDS
        
        # Test connection on initialization
        try:
            self.redis.ping()
        except RedisError as e:
            raise RuntimeError(f"Failed to connect to Redis: {str(e)}")

    def get(self, key: str):
        try:
            cached_data = self.redis.get(key)
            if cached_data:
                return json.loads(cached_data)
            return None
        except (RedisError, json.JSONDecodeError) as e:
            # Log error here if you have logging setup
            return None

    def set(self, key: str, value: dict):
        try:
            self.redis.set(
                key,
                json.dumps(value),
                ex=self.expire
            )
        except (RedisError, TypeError) as e:
            # Log error here if you have logging setup
            pass

cache_service = CacheService()