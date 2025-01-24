# Generator Function with yield
# TODO: Write a generator function that yields even numbers up to a specified limit.
# * NOTE: Here yield will return the number but will not stop further execution of the function
# * This generator function will return a generator object which can be used to iterate over
def even_numbers_generator(limit):
    for number in range(2, limit + 1, 2):
        yield number


limit = 10


for even_number in even_numbers_generator(limit):
    print(even_number)
