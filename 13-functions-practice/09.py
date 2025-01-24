# Recursive Function
# TODO: Create a recursive function to calculate the factorial of a number.
def factorial(number):
    # Base condition
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


# * NOTE: Give a positive number
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
