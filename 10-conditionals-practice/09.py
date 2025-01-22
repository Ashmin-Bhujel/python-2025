# Pet Food Recommendation
# TODO: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
pet_species = ("dog", "cat")
species = input("Enter you pet's species [Dog/Cat]: ").lower()


if species not in pet_species:
    print("Sorry we don't have information on that species")
    exit()


pet_age = int(input("Enter the age of your pet: "))


if pet_age < 1:
    print("Invalid pet age!")
    exit()


pet_food = ""

if species == "dog":
    pet_food = "puppy food" if pet_age < 2 else "adult dog food"
else:
    pet_food = "senior cat food" if pet_age > 5 else "junior cat food"


print(f"Your pet's food is {pet_food}")
