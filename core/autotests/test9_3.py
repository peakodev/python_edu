def caching_fibonacci(cache={0: 0, 1: 1}):
    def fibonacci(n):
        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


print(caching_fibonacci()(5))
print(caching_fibonacci()(15))
print(caching_fibonacci()(45))
print(caching_fibonacci()(50))
