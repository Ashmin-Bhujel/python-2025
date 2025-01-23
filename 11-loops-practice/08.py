# List Uniqueness Checker
# TODO: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "banana", "mango"]
unique_items = set()
is_there_duplicates = False


for item in items:
    if item in unique_items:
        print(f"The duplicate item is {item}")
        is_there_duplicates = True
        break
    else:
        unique_items.add(item)


if not is_there_duplicates:
    print("There are no duplicate items")
