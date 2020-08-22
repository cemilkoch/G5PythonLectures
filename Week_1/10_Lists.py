# Lists can contain numbers and strings together

# Creating a List []
list1 = []
print("Empty List", list1)

# Creating a List of Numbers
list2 = [20, 30, 35, 40]
print("List of numbers", list2)

# Creating a list of strings
list3 = ["Java", "C++", "Python", "Javascript", "SQL"]

# Accessing the items
print("Index number 1", list3[1])
print("Index number 2", list3[2])

# Create a multi-dimensional list(Nested Lists)
shopping_list = [["Oranges", "Bananas", "Apples"], ["Cheese", "Milk", "Eggs"]]
print(shopping_list)
print(shopping_list[0][2])

# Lists can have duplicate values
list4 = [1, 1, 2, 3, 3, 3, 5, 5, 5]
print(list4)

# Lists can have mixed type of values(numbers and strings)
list5 = [2, 5, "Silicone Labs", 10.6, True, ["eggs", "milk"]]
print(list5)
print(len(list5))

# Boolean type
status = True
status = False
