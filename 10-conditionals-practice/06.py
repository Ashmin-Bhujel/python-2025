# Coffee Customization
# TODO: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
order_sizes = ("small", "medium", "large")
order_size = input("Enter your order size [Small/Medium/Large]: ").lower()


if order_size not in order_sizes:
    print("Sorry, Invalid order size!")
    exit()


is_extra = True if input("Do you want extra shot? [y/n]: ").lower() == "y" else False


if is_extra:
    print(f"Here is your {order_size} size coffee with extra shot of expresso")
else:
    print(f"Here is your {order_size} size coffee")
