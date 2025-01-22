# Find the First Non-Repeated Character
# TODO: Given a string, find the first non-repeated character.
user_input = input("Enter a string: ")


for character in user_input:
    if user_input.count(character) == 1:
        print(f"The first non-repeating characer is {character}")
        break
