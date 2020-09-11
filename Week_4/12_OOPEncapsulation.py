class Mammal:

    def __init__(self, species):
        # Private variable __
        self.__species = species

    def show_species(self):
        print("I am a", self.__species)

    def make_sound(self):
        print("Grrrr....")


class Dog(Mammal):

    def __init__(self):
        super().__init__("Dog")

    def make_sound(self):
        print("Woof woof")


dog = Dog()
dog.show_species()
