# Functions

# Creating(defining) a function
# def == defining a function
# function name
# Parameters(Arguments) optional
# body = code statements
def name_of_func():
    print('hello')


# Calling the function name_of_func()
name_of_func()


def say_hello():
    print("Hello, How are you?")


say_hello()


# Create a function with 1 parameter
def greeting(name):
    print("Welcome", name)


# Call the function
greeting("John")
greeting("Michael")
greeting("Cemil")


# Create a function with 2 parameters
def greeting2(first, last):
    print("Welcome", first, last)


# Calling function greeting2
greeting2("Cemil", "Koc")
greeting2("Selim", "Erciyas")

first_name = "Michael"
last_name = "Chris"
greeting2(first_name, last_name)


# Create a function to add 2 numbers
def add(num1, num2):
    print(num1 + num2)


# Call add function
add(20, 100)
add(200, 300)

print("\n**************\n")


# Create a function to add a list of numbers
def add_list(lst):
    add = 0  # To store the addition
    for i in lst:
        add = add + i
    print("The result is", add)


# Call add_list() function
add_list([5, 4, 3, 2, 1])
lst = [1, 2, 3, 4, 5, 6, 7, 8]
add_list(lst)

