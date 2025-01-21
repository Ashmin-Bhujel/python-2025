# Weather Activity Suggestion
# TODO: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
activity = {
    "sunny": "go for a walk",
    "rainy": "read a book",
    "snowy": "build a snowman",
}
weather = input("How is weather today? [Sunny/Rainy/Snowy]: ").lower()


if weather not in activity:
    print("Sorry, cannot suggest activity right now!")
    exit()


print(f"You should {activity[weather]}")
