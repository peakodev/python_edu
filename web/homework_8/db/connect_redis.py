import redis
from redis_lru import RedisLRU

from .conf import config

host = config.get('Redis', 'host')
port = config.get('Redis', 'port')

client = redis.StrictRedis(host=host, port=port, password=None)
cache = RedisLRU(client)
