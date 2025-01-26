# Basic Class and Object
# TODO: Create a Car class with attributes like brand and model. Then create an instance of this class.
# Car class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# Instance of the Car class (object)
my_car = Car("Honda", "CR-V")
