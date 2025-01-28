# Multiple Inheritance
# TODO: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Battery:
    @staticmethod
    def get_battery_info():
        return "Electric cars use electric charges from batteries to operate"


class Engine:
    @staticmethod
    def get_engine_info():
        return "Electric cars' engines do not operate on petrol or diesel"


class ElectricCar(Battery, Engine):
    pass


print(ElectricCar.get_battery_info())
print(issubclass(ElectricCar, Battery))
print(ElectricCar.get_engine_info())
print(issubclass(ElectricCar, Engine))
