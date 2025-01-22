# Sum of Even Numbers
# TODO: Calculate the sum of even numbers up to a given number n.
n = 0


while True:
    n = int(input("Enter a number: "))

    if n < 0:
        print("Please enter a positive number!")
    else:
        break


sum = 0


for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i


print(f"The sum of even numbers up to {n} is {sum}")
