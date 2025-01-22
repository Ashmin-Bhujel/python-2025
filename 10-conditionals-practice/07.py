# Password Strength Checker
# TODO: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
user_password = input("Enter your password to check its strength: ")
password_length = len(user_password)


if password_length < 1:
    print("Invalid input!")
    exit()


password_strength = ""


if password_length < 6:
    password_strength = "weak"
elif password_length <= 10:
    password_strength = "medium"
else:
    password_strength = "strong"


print(f"Your password's strength is {password_strength}")
