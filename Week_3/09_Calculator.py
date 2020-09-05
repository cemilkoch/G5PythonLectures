# A simple Calculator Program

def add(x, y):
    """This function adds two numbers"""
    return x + y


def subtraction(x, y):
    """This function subtracts two numbers"""
    return x - y


def divide(x, y):
    """This function divides two numbers"""
    return x / y


def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y


print("Select an operation")
# Operations list to check if the user entered operation is in the list
operations = ['+', '-', '/', '*']


# Loop to check if the operation is a valid operation
# If the user enters invalid operator we are going make them reenter an operator
choice = ""
status = True
while status:
    choice = input()
    if choice in operations:
        status = False
    else:
        print("Invalid operator, choose again")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if choice == '+':
    print(num1, "+", num2, '=', add(num1, num2))

elif choice == '-':
    print(num1, "-", num2, '=', subtraction(num1, num2))

elif choice == '/':
    print(num1, "/", num2, '=', divide(num1, num2))

else:
    print(num1, "*", num2, '=', multiply(num1, num2))

