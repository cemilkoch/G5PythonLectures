# Create a function to return the absolute value of a number
# -5 returned as 5

def absolute_val(number):
    if number >= 0:
        return number
    else:
        return -number


print(absolute_val(-5))
print(absolute_val(6))


def absolute_val2(n):
    return abs(n)


print(absolute_val2(-5))


# Local variables and global variables
# Local variable is a variable created within the function
# Global variable is declared in the main python file

def my_function():
    x = 10  # local variable
    print("Value inside function:", x)


my_function()
x = 20
print("Value outside the function", x)

y = 20


def my_function2():
    global y
    y = 25
    print("Value inside function", y)


print("Value outside the function", y)
my_function2()


# *args
# It is used to add multiple amount of parameters
def function(name):
    print("Hello", name)


function("Cemil")


def function2(x, y, z, t):
    print(x + y + z + t)


function2(1, 2, 3, 4)


# Create a function to enter different amount of numbers to add
# *args (non keyword arguments)
def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)


add(1)
add(1, 2, 3, 4, 5)
add(3, 5)


def greet(name):
    print("Welcome", name)


name = input("Enter a name: ")
greet(name)


# Get the amount of numbers that user wants to add
numbers = int(input("How many numbers do you want to add? "))
lst = []
for i in range(numbers):
    number = int(input("Enter a number: "))
    lst.append(number)


