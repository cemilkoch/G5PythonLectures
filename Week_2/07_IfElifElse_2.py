# How to check if a number is even?
# % will return remainder
# Number % 2 == 0 if you divide a number by 2 and get 0 it means that
# the number is even

# Challenge!
# Get a number from the user(input) and check if it is even or odd

# number = int(input("Please enter a number: "))
#
# if number % 2 == 0:
#     print(number, "is even")
# else:
#     print(number, "is odd")

# Challenge 1
# Take length from the user(input)
# Take width from the user
# Check if it is a square or not

# Challenge 2
# Take 2 numbers from the user(input) and print the greatest among them

# Challenge 1
# length = int(input("Enter length : "))
# width = int(input("Enter width : "))
#
# if length == width:
#     print("It is a square")
# else:
#     print("It is not a square")

# Challenge 2

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
if number1 > number2:
    print(number1, "is bigger")
elif number1 == number2:
    print(number1, number2, "are equal")
else:
    print(number2, "is bigger")
