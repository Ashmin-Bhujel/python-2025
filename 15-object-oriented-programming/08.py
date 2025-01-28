# Class Inheritance and isinstance() Function
# TODO: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


car = ElectricCar("Tesla", "Model S", "98kWh")
print(isinstance(car, Car))
# True
print(isinstance(car, ElectricCar))
# True
