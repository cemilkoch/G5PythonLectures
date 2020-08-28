# Write a program that:
# Requests the user's name
# Requests the user's age
# prints a message saying whether the user is eligible to vote or not
# 18 and greater can vote

name = input("Enter a name: ")
age = int(input("Enter an age: "))

if age >= 18:
    print(name + ", you are eligible to vote")
else:
    print(name + ", you are ineligible to vote")
