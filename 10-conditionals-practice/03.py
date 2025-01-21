# Fruit Ripeness Checker
# TODO: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe).
ripeness = {
    "green": "unripe",
    "yellow": "ripe",
    "brown": "overripe",
}
color = input("What is the color of the Banana? [Green/Yellow/Brown]: ").lower()


if color not in ripeness:
    print("Sorry, cannot identify the ripeness of the Banana!")
    exit()


print(f"The Banana is {ripeness[color]}")
