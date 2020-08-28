# Calculator Example
# We are going to get 2 numbers from the user
# We are going to ask for an operator(+, -, *, /)

x = int(input("First number: "))
y = int(input("Second number: "))

operator = input("Enter the first letter of the operation[A, S, M, D] ").upper()

if operator == 'A':
    print(x + y)
elif operator == 'S':
    print(x - y)
elif operator == 'M':
    print(x * y)
elif operator == 'D':
    print(x / y)
else:
    print("Invalid operator")
