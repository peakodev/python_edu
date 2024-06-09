import os

from dotenv import load_dotenv
import redis


load_dotenv()


r = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), password=None)

r.set('foo', 'bar', ex=10)

print(r.get('foo').decode())

r.set('foo', 'bar2')

print(r.get('foo'))