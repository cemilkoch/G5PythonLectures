# If statement is used for decision making
# If statement has body of code which runs only when the given condition is True
# If the condition is false, then else statement runs

# Syntax for If statement
"""
if case1:  if case1 is True perform action
    perform action
elif case2:  if case2 is True perform action2
    perform action2
else:  case1 and case2 are incorrect then else statement runs
    perform action3
"""

condition = True

if condition:
    print("It is True")

age = 80
if age >= 80:
    print("You are too old")

x = 5
y = 10
z = 25

# = assignment operator
# == is to compare 2 values

if x > y:  # is x bigger than y? yes(True) or no(False)
    print("x is greater than y")
elif x < z:  # is x less than z? yes(True) or no(False)
    print("x is less than z")
else:
    print("If and elif statements never worked")

location = "Auto Shop"

if location == "Auto Shop":
    print("Welcome to the Auto Shop")
elif location == "Bank":
    print("Welcome to the Bank")
else:
    print("I don't know where you are")

person = "Sammy"

if person == "Sammy":
    print("Welcome Sammy")
else:
    print("I don't know who you are")

person_2 = "Sammy"

if person_2 == "Sammy":
    print("Welcome Sammy")
elif person_2 == "George":
    print("Welcome George")
else:
    print("What is your name?")

name = input("What is your name? ")

if name == "Jimmy":
    print("Welcome Jimmy")
elif name == "Michael":
    print("Welcome Michael")
else:
    print("I don't know you")
