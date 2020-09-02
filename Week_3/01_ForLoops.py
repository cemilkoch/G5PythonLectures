# Program to find the sum of all numbers in a list

numbers = [6, 5, 4, 11, 25, 100, 90]
add = 0  # 26

for i in numbers:
    add += i  # add = add + i

print("Result", add)

# program to multiply all the numbers in the list
multiply = 1
for i in numbers:
    multiply = multiply * i

print("Result of multiplication", multiply)

# Iterating through a list using slicing []
genre = ['rock', 'pop', 'jazz', 'classical']
print(len(genre))

for i in range(len(genre)):
    print("I like", genre[i])

print("\n*************\n")

tuple1 = (1, 2, 3, 4, 5)

for i in tuple1:
    print(i)

list1 = [(2, 4, 14), (6, 8, 16), (10, 12, 18)]

for tup in list1:
    print(tup)

# Unpacking a tuple
for t1, t2, t3 in list1:
    print(t1, t2, t3)

# Iterating through the dictionary
d = {'key1': 1, 'key2': 2, 'key3': 3}
# keys()
print(d.keys())
# values()
print(d.values())
# items()
print(d.items())

for k, v in d.items():
    print(k, v)

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

# Challenge !
# Create an empty list
# Using a for loop add even numbers from 0 - 41 to the empty list
# print out the list

lst = []
# for i in range(41):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)

for i in range(0, 41, 2):
    lst.append(i)
print(lst)

print('\n****************\n')
# Challenge !
# Use the list with the even numbers[0,2....40]
# Make a new list which will store square values of each element
# new_list = [0, 4, 16, .....]
squares = []
for i in lst:
    squares.append(i ** 2)
print(squares)
