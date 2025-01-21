# Movie Ticket Pricing
# TODO: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
age = int(input("Enter your age: "))


if age <= 0:
    print("Invalid age!")
    exit()


is_wednesday = True if input("Is it Wednesday today? [y/n]: ").lower() == "y" else False
ticket_price = 12 if age >= 18 else 8
discount = 2


if is_wednesday:
    ticket_price -= discount


print(f"Your ticket price is ${ticket_price}")
