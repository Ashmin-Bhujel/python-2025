# Prime Number Checker
# TODO: Check if a number is prime.
number = 0
is_prime = True


while True:
    number = int(input("Enter a number greater than 1: "))

    if number <= 1:
        print("Please try again!")
    else:
        break


# * NOTE: We can reduce the calculations by only checking upto half of the number
for i in range(2, int(number / 2) + 1):
    if number % i == 0:
        is_prime = False
        break


print(f"{number} is a prime number: {is_prime}")
