# The class is a blueprint that defines the nature of objects
# Class is a blueprint where we can create objects from it

# Create a class called Sample
class Sample:
    pass


# Creating a new object from Sample Class
obj = Sample()
print(type(obj))
print(type("String"))


# Creating Class Computer
class Computer:
    # Class Variables, attributes
    model = "Apple"
    color = "Silver White"
    storage = "512 GB"
    ram = "16 GB"


# Creating object from Computer Class
computer1 = Computer()
print(type(computer1))
print(computer1)

# Calling class variables
print("Computer model", computer1.model)
print("Computer color", computer1.color)
print("Computer storage", computer1.storage)
print("Computer RAM", computer1.ram)

# Creating a second object from Computer Class
computer2 = Computer()
computer2.model = "Windows"

print(computer2.model)
print(computer2.color)
print(computer2.ram)
print(computer2.storage)
