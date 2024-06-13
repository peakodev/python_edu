import time
import logging
from functools import wraps
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count, get_logger, log_to_stderr


log_to_stderr()
logger = get_logger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(processName)s : %(message)s')
handler = logger.handlers[0]  # Стандартний обробник для log_to_stderr
handler.setFormatter(formatter)


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


TEST_DATA = (128, 255, 99999, 10651060)
EXPECTED = [
    [1, 2, 4, 8, 16, 32, 64, 128],
    [1, 3, 5, 15, 17, 51, 85, 255],
    [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999],
    [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395,
     532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
]


def test_factorize(results):
    for result, exp in zip(results, EXPECTED):
        assert result == exp, f"Failed test case: {result} != {exp}"
    logger.info("All tests passed!")


@time_execution
def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)


@time_execution
def factorize(*numbers):
    logger.info("Start factorize")
    return [find_factors(number) for number in numbers]


@time_execution
def factorize_multiprocessed(*numbers):
    logger.info("Start factorize_multiprocessed")
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        results = list(executor.map(find_factors, numbers))
    return results


if __name__ == '__main__':
    test_factorize(factorize(*TEST_DATA))
    test_factorize(factorize_multiprocessed(*TEST_DATA))
