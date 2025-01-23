# Factorial Calculator
# TODO: Compute the factorial of a number using a while loop.
factorial = 1


while True:
    n = int(input("Enter a number: "))

    if n < 1:
        print("Please enter a positive number!")
    else:
        break


i = 1
while i <= n:
    factorial *= i
    i += 1


print(f"The factorial of the given number {n} is {factorial}")
