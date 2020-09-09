class Car:
    # * The goal of __init__ function is to initialize(assign values) to
    #   the variables of the class when you create an object
    def __init__(self, brand, model, year, doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.doors = doors


car1 = Car("Toyota", "Corolla", 2019, 4)
car2 = Car("BMW", "i8", 2019, 2)
car3 = Car("Toyota", "Avolon", 2018, 4)

print("car3 attributes:")
print("Brand:", car3.brand)
print("Model:", car3.model)
print("Year:", car3.year)
print("Doors:", car3.doors)
