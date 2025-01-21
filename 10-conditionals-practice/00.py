# Age Group Categorization
# TODO: Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
age = int(input("Enter your age: "))


if age <= 0:
    print("Invalid age!")
    exit()


if age < 13:
    print("You're a child")
elif age < 20:
    print("You're a teenager")
elif age < 60:
    print("You're an adult")
else:
    print("You're a senior")
