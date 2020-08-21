# input is built-in function and it will ask the user to enter characters
# By default input function will return string

greeting = "Hello"
name = input("Please enter your name: ")
print(greeting, name)
print(type(name))

age = int(input("Please enter your age: "))
print("Your age is", age)
print(type(age))

miles = float(input("How many miles did you run? "))
print("You burned ", (miles * 250), "calories")

# Data Type Conversion
# int to float
integer = 75
floating = float(integer)

# String to int
str_number = "28"
int_number = int(str_number)

