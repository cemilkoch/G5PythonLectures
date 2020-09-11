class Employee:

    # Constructor for Employee Class
    def __init__(self, name, salary, department):
        print("This is an Employee Class Constructor")

        self.name = name
        self.salary = salary
        self.department = department

    def information(self):
        print("Employee information:")
        print(f"Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}")

    def update_department(self, new_department):
        self.department = new_department


class Manager(Employee):
    manager_id = ""

    def __init__(self, name, salary, department, manager_id):
        super().__init__(name, salary, department)
        self.manager_id = manager_id

    def apply_raise(self, amount):
        print("Applying a raise")
        self.salary += amount

    def manager_information(self):
        super().information()
        print(f"ID: {self.manager_id}")


        # print("Employee information:")
        # print(f"Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}"
        #       f"\nID: {self.manager_id}")


manager = Manager("Abby Lindbergh", 5000, "Human Resources", 105)
# manager.information()
manager.update_department("Data Analyst")
manager.information()
manager.apply_raise(500)
print()
manager.manager_information()

