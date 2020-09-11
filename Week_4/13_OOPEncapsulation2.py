class Automobile:  # Parent Class

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # Getters: They help us to access the private variables from a class(Accessors)
    # Setters: They help us to set the value to private variables in a class(Mutators)

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price


class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)
        self.__doors = doors

    def get_doors(self):
        return self.__doors

    def set_doors(self, doors):
        self.__doors = doors


audi = Car("Audi", "A4", 75000, 9000, 4)
print("The following car is in the inventory")
print("Make", audi.get_make())
print("Model", audi.get_model())
print("Mileage", audi.get_mileage())
audi.set_mileage(80000)
print("New mileage", audi.get_mileage())

# Create Truck class inherit from Automobile Class
# add drivetype to the constructor
# create getters and setters for truck class

