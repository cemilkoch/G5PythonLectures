# Inheritance is a "is a" relationship
# Inheritance enables us to define a class that takes all the functionality and chracteristics from
# superclass(parent) and allows us to add more


# Creating Class Things SuperClass
class Things:
    pass


# Creating Inanimate Class
class NotAlive(Things):
    pass


# Creating Animate Class
class Animate(Things):
    pass


# Creating Pencil class
class Pencil(NotAlive):
    pass


# Creating Animals Class
class Animals(Animate):

    def eat(self):
        print("Animal is Eating")

    def breathe(self):
        print("Breathing")


# Creating Mammals Class
class Mammals(Animals):

    def eat(self):
        print("Mammals feed with milk")


class Cat(Mammals):

    def speak(self):
        print("Meow")


class Dog(Mammals):

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "is barking")

    def breathe(self):
        print(self.name, "is breathing")


harold = Cat()
harold.eat()
harold.breathe()

reginald = Dog("Reginald")
reginald.bark()
reginald.breathe()
