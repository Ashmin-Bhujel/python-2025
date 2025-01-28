# Debugging Function Calls
# TODO: Create a decorator to print the function name and the values of its arguments every time the function is called.
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args) if args else "N/A"
        kwargs_value = (
            ", ".join(f"{k}: {v}" for k, v in kwargs.items()) if kwargs else "N/A"
        )
        print(
            f'"{func.__name__}" function was called with args value {args_value} and kwargs value {kwargs_value}'
        )
        return func(*args, **kwargs)

    return wrapper


@debug
def greet(name, greeting):
    print(f"{greeting}, {name}")


@debug
def say_hello():
    print("Hello")


greet("Ashmin", greeting="Hello")
say_hello()
