# Multiplication Table Printer
# TODO: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
n = int(input("Enter a number: "))
total_iterations = 10
iteration_to_be_skiped = 5


for i in range(1, total_iterations + 1):
    if i == iteration_to_be_skiped:
        continue

    print(f"{n} x {i} = {n * i}")
