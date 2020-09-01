# for variable in [value1, value2, etc.]:
#   statement
#   statement
#   etc.

languages = ["Java", "C++", "Ruby", "Python"]

for language in languages:
    print(language, end=" ")
else:
    print()
    print("The loop finished iterating through the items")
# Else statement will work after all the items in the
# sequence(list, string, tuple, etc.) have been used

print("\n", "*" * 15, "\n")

# End the loop if i gets larger than 5
for i in range(10):
    if i > 5:
        break  # break will exit the loop and it will not use the rest of the sequence
    print(i)

print("\n", "*" * 15, "\n")

text = "Learning Python"

for letter in text:
    print(letter)
    # break the loop when it sees 'g' or 'y'
    if letter == 'g' or letter == 'y':
        break

print("Out of the loop")

print("\n", "*" * 15, "\n")

for i in range(1, 11):
    # Print all the numbers from 1 - 10 but skip 8
    if i == 8:  # if i is equal to 8, continue to next item(skip number 8)
        continue
    print(i)

print("\n", "*" * 15, "\n")

numbers = list(range(1, 11))
# Get each number's square value
# 1 ^ 2 = 1
# 2 ^ 2 = 4
# 3 ^ 2 = 9
# 4 ^ 2 = 16 ....

# ** = square value
for i in numbers:
    print(i, "^ 2 = ", i ** 2)

print("\n", "*" * 15, "\n")

# print numbers 1 - 10 in reverse order
# 10, 9, 8, 7, .... ,1

for i in range(10, 0, -1):
    print(i)

print("\n", "*" * 15, "\n")

# Create a program to add numbers to a list
# Ask how many numbers the user wants to add
# Get the numbers from the user and add it to the list
# input : How many numbers you want to add? 2
# Enter a number 1
# Enter a number 3
# Output 1,3

list_size = int(input("How many numbers do you want to add: "))
lst = []  # This empty list will be appended depending on the user input
for i in range(list_size):
    numbers = int(input("Enter number: "))
    lst.append(numbers)

print(lst)

print("\n", "*" * 15, "\n")

numbers_list = [0.1, 45, 235, 0.45, 2, 95, 63, -0.5]
# Using a for loop, generate a new list containing every object in
# the numbers_list multiplied by 10
# Hint : Use * operator to perform a multiplication
