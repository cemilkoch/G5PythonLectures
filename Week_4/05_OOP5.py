class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "is eating")

    def meow(self):
        print(self.name, "is meowing")

    def cat_info(self):
        print(self.name, "is", self.age, "years old.")


mia = Cat("Mia", 3)
mia.eat()
mia.meow()

boncuk = Cat("Boncuk", 4)
boncuk.eat()
boncuk.meow()

mia.cat_info()
boncuk.cat_info()

