# Class Variables
# TODO: Add a class variable to Car that keeps track of the number of cars created.
class Car:
    # Class variable
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # * NOTE: Access the class variable with the class name
        Car.total_cars += 1


car1 = Car("Honda", "CR-V")
print(f"Total Cars: {Car.total_cars}")
# 1

car2 = Car("Toyota", "Corolla")
car3 = Car("Tata", "Nexon")
print(f"Total Cars: {Car.total_cars}")
# 3
