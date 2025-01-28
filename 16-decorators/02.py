# Cache Return Values
# TODO: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
import time


def cache(func):
    cached_results = {}

    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]

        result = func(*args)
        cached_results[args] = result
        return result

    return wrapper


@cache
def long_running_function(first, second):
    time.sleep(5)
    return first + second


print(long_running_function(2, 4))
print(long_running_function(2, 4))
print(long_running_function(6, 8))
