# List Methods

# Creating a list
list1 = []
print(list1)

# Adding element into list1 append()
list1.append(10)
list1.append(5.24)
list1.append(15)

print("List after adding elements", list1)

# insert() method
container = ["TV"]
container.insert(2, "Bicycle")
container.insert(1, "Microwave")
print(container)

container.insert(0, "Closet")
print(container)

# extend() Method
list2 = [1, 2, 3, 4]
list2.extend([5, 6, 7, 8])
print(list2)

# Updating elements of a list
list3 = ["Fish", "Cat", "Dog"]
list3[0] = "Bird"
print(list3)

# Deleting items from a list
del list3[1]
print("My cat died", list3)

# remove(), pop(), clear()
ch_list = ['A', 'B', 'C']
ch_list.remove('B')
print(ch_list)

# pop()
ch_list.pop(0)
print(ch_list)

# clear()
ch_list.clear()
print(ch_list)

# Challenge !
list4 = [4, 4, ["Ford", "BMW", "Honda", "Toyota"], [2016, 2017]]
# remove "Ford"
# insert 2018 and 2019 in the nested list [2016, 2017, 2018, 2019]
list4[2].pop(0)
list4[3].extend([2018, 2019])
print(list4)


