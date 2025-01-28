# Static Method
# TODO: Add a static method to the Car class that returns a general description of a car.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Static method
    @staticmethod
    def general_description():
        return "Cars are vehicles with wheels, typically powered by an engine, used for transportation."


print(Car.general_description())
