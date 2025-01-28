# Property Decorators
# TODO: Use a property decorator in the Car class to make the model attribute read-only.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @property
    # * NOTE: Property decorator make the model attribute read-only attribute
    def model(self):
        return self.__model


car = Car("Tesla", "Model S")
print(car.model)
