# Reverse a String
# TODO: Reverse a string using a loop.
original = ""
reversed_string = ""


while True:
    original = input("Enter a string: ")
    string_length = len(original)

    if string_length < 1:
        print("Please enter a valid string!")
    else:
        break


for character in original:
    reversed_string = character + reversed_string


print(f"The reversed string is {reversed_string}")
