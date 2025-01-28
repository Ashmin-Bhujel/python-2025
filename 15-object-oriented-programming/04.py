# Polymorphism
# TODO: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battry_size):
        super().__init__(brand, model)
        self.battery_size = battry_size

    def fuel_type(self):
        return "Electric Charge"


car1 = Car("Honda", "CR-V")
car2 = ElectricCar("Tesla", "Model S", "98kWh")
print(car1.fuel_type())
print(car2.fuel_type())
