class Person:  # Superclass(Parent, Base)

    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


class Student(Person):  # SubClass(Child)

    student_id = ""

    def __init__(self, name, age, id):
        # Super keyword is calling(invoking) parent class constructor(__init__)
        # super().__init__(name, age)
        Person.__init__(self, name, age)
        self.student_id = id

    def show_student_id(self):
        print(self.student_id)


# Creating object from Person Class
person = Person("Michael", 35)
person.show_name()
person.show_age()

# Creating object from Student Class
student = Student("Max", 25, 4509)
student.show_name()
student.show_age()
student.show_student_id()
