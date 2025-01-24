# Function with *args
# TODO: Write a function that takes variable number of arguments and returns their sum.
# * NOTE: The args parameter will get a tuple with all the arguments
def add_all(*args):
    sum = 0

    for arg in args:
        sum += arg

    return sum


result = add_all(1, 2, 3, 4, 5, 6)
print(f"The sum of given arguments are {result}")
