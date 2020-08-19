# Rules for Variable Names
# Variable names can't start with a number
# Variable names can't contain spaces, instead we can use underscores snake_case camelCase
# Variables can't contain symbols : '<>!$@

my_cats = 4
print(my_cats)

my_cats = 6
print(my_cats)

b = 10

# Reassigning Variables
b = b + b + b

print(b)

c = 20
c = c + 10
print(c)

# There is a shortcut for writing this code c = c + 10
# +=
c += 10  # c = c + 10
print(c)

a = 4
a *= 3
print(a)

y = 25
y /= 5
print(y)

# Dynamic Typing
number = 55
# this will store 55 in the memory and binds name number to it
# After running the code the number will be int
print(type(number))

number = "Hello"
print(type(number))
