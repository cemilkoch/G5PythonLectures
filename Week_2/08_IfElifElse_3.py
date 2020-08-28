# Nested IF Statements
# We can have if elif else statement inside another if elif else statement
# This is called nested if statements

first_name = "Michael"
last_name = "Jackson"

if first_name == "Michael":
    if last_name == "Johnson":
        print("Welcome Michael Johnson")
    else:
        print("Michael, what is your last name?")
elif first_name == "Sammy":
    if last_name == "Jackson":
        print("Welcome Sammy Jackson")
    else:
        print("Sammy, what is your last name?")
else:
    print("Who are you?")

# I will write a program to check if a number is positive
# If the number is positive, I will also check if it is even or odd number
# % modulo | number % 2 == 0 even number check

number = -10

if number > 0:
    print("The number is positive")
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, 'is odd')
else:
    print("The number is negative")
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, 'is odd')

print("\n*************\n")

# Check if the number is positive or 0 or negative
number2 = int(input("Enter a number: "))

if number2 >= 0:  # This will check if the number is greater than or equal to 0
    if number2 == 0:  # check if the number is 0
        print("The number you have entered is zero")
    else:
        print("Number is positive")
else:  # if statement fails
    print("Negative number")
