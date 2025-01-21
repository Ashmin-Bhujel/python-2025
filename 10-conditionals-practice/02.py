# Grade Calculator
# TODO: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
score = int(input("Enter your score: "))
grade = ""


if score < 0 or score > 100:
    print("Invalid score!")
    exit()


if score < 60:
    grade = "F"
elif score < 70:
    grade = "D"
elif score < 80:
    grade = "C"
elif score < 90:
    grade = "B"
else:
    grade = "A"


print(f"You grade is {grade}")
