# Inheritance
# TODO: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
# Parent class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


# Child class
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


car = Electric_Car("Tesla", "Model S", "98kWh")

print(car.full_name())
