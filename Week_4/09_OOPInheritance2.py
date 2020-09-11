class Mammals:
    # Constructor for Mammals Class
    def __init__(self, name):
        print(name, "is a warm blooded animal")


class Dog(Mammals):
    # Constructor for Dog Class
    def __init__(self):
        print("Dog has four legs")
        # Calling parent class constructor using super keyword
        super().__init__("Dog")


dog = Dog()
mammal = Mammals("Cat")

