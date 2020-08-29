# for variable in [value1, value2, etc.]:
#   statement
#   statement
#   etc.

# The variable is assigned to first value in the list
# then the statements in the block will be executed
# Then, variable is assigned to the next value
# and the statements in the block will be executed again.
# This continues until the variable has been assigned to the last value in the list

c = ['orange', 'banana', 'apple']
# print every item
print(c[0])
print(c[1])
print(c[2])

for element in c:
    print(element)

# For loops iterate over a given sequence
prime = [2, 3, 5, 7]
for i in prime:
    print(i, end=' ')
print()
# Range is a built-in function that returns a sequence
# range(start:end:step)
# range(number) start from 0 to number - 1

# Prints out the number 0, 1, 2, 3, 4
for i in range(5):
    print(i)

print()
# prints out 3, 4, 5
for x in range(3, 6):
    print(x)
print()

# prints out 3, 5, 7
for x in range(3, 8, 2):
    print(x)

# list creates a list
list1 = list(range(10))
print(list1)

# Add even numbers using range function
list2 = list(range(0, 11, 2))
print(list2)

# list of numbers from 0 - 10
list3 = list(range(11))
print("list3 :", list3)

for i in list3:
    if i % 2 == 0:
        print(i, end=' ')
print("\n")

for num in list3:
    if num % 2 == 0:
        print(num)
    else:
        print("Odd number")

# break and continue
# break is used to exit a for loop
# continue is used to skip the current block, and return to the for loop

# print only odd numbers : 1, 3, 5, 7, 9
for i in range(10):  # i = 4
    if i % 2 == 0:
        continue
    print(i)

print("After the break")
# when you use break statement it will exit the loop
# it will not iterate through the next items
for i in range(10):  # i = 1
    if i % 2 == 1:
        break
    print(i)
print()
# print 1, 2, 3
for letter in [1, 2, 3, 4, 5, 6]:  # letter = 4
    if letter == 5:
        break
    print(letter)  # 1 2 3

print()

# continue
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list4:
    if i == 3 or i == 5 or i == 7:
        continue
    print("i :", i)
