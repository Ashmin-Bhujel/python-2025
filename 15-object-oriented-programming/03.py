# Encapsulation
# TODO: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
class Car:
    def __init__(self, brand, model):
        # * NOTE: To make an attribute private add "__" infront of its name
        self.__brand = brand
        self.model = model

    # Getter method for brand attribute
    def get_brand(self):
        return self.__brand

    # Setter method for brand attribute (Bonus)
    def set_brand(self, new_brand):
        self.__brand = new_brand


car = Car("Tesla", "Model S")
print(car.get_brand())
