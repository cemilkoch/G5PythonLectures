class Employee:

    def __init__(self, first, last, salary):
        # instance variables
        self.first = first
        self.last = last
        self.salary = salary

    def apply_raise(self):
        self.salary = int(self.salary) * 1.04


emp1 = Employee("John", "Son", 6000)
print("Employee 1 salary before raise:", emp1.salary)
emp1.apply_raise()
print("Employee 1 salary after raise:", emp1.salary)
