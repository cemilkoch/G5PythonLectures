# __init__ function for the class
# __init__ function == Constructor
# * The goal of __init__ function is to initialize(assign values) to
#  the variables of the class when you create an object
# * The __init__ function will always be called when object is created

class Car:
    brand = "Toyota"
    model = "Corolla"
    year = 2019
    doors = 4

    def __init__(self):
        print("The object is created and init function is running")


car1 = Car()
car2 = Car()
car3 = Car()
