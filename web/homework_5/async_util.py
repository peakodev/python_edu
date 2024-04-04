from time import time

from logger import logger


def async_timeit(func):
    async def wrapped(*args, **kwargs):
        name = f"func {func.__name__} with {args} {kwargs}"
        logger.debug(f"Start {name}")
        start = time()
        try:
            return await func(*args, **kwargs)
        finally:
            logger.debug(f"End {name}. Spend {(time() - start):4f}")
    return wrapped
