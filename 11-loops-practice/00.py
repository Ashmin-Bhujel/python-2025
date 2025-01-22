# Counting Positive Numbers
# TODO: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_count = 0


for number in numbers:
    if number > 0:
        positive_count += 1


print(f"There are {positive_count} positive numbers")
