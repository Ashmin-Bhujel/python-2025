# Timing Function Execution
# TODO: Write a decorator that measures the time a function takes to execute.
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_runtime = end_time - start_time
        print(f"{func.__name__} ran for {total_runtime}s")
        return result

    return wrapper


@timer
def test_func(n):
    time.sleep(n)
    return "Hello from test_func"


print(test_func(2))
