# Transportation Mode Selection
# TODO: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
distance = int(input("Enter the distance to be traveled: "))


if distance < 1:
    print("Invaid distance!")
    exit()


mode_of_transportation = ""


if distance < 3:
    mode_of_transportation = "walk"
elif distance <= 15:
    mode_of_transportation = "bike"
else:
    mode_of_transportation = "car"


print(f"Your recommended mode of transportation is {mode_of_transportation}")
