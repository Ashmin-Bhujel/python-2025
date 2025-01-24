# Function with **kwargs
# TODO: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
# * NOTE: The kwargs will get a dictionary with all the named arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Ashmin", age=21, address="Earth")
