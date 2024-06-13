import time
from functools import wraps
from multiprocessing import Pool, cpu_count


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


TEST_DATA = (128, 255, 99999, 10651060)


def test_factorize(a, b, c, d):
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("All tests passed!")


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
    print("Start factorize")
    return [find_factors(number) for number in numbers]


test_factorize(*factorize(*TEST_DATA))


@time_execution
def factorize_multiprocessed(*numbers):
    print("Start factorize_multiprocessed")
    with Pool(cpu_count()) as pool:
        result = pool.map(find_factors, numbers)
    return result


test_factorize(*factorize_multiprocessed(*TEST_DATA))
