from time import time
from functools import wraps

def async_timeit(func):
    # def wrapper(func):
    #     @wraps(func)
    async def wrapped(*args, **kwargs):
        print(f"Start function {func.__name__} with {args} {kwargs}")
        start = time()
        try:
            return await func(*args, **kwargs)
        finally:
            print(f"End function {func.__name__}. Spend {(time() - start):4f}")
    return wrapped
    # return wrapper
