# Functions with return keyword
# The return allows you to save the result of a function as a variable
# The print function inside the function just displays the output to you

# Void Function
def print_add(num1, num2):
    print(num1 + num2)


print_add(15, 30)


# Function(Fruitful) with Return
def return_add(num1, num2):
    return num1 + num2


addition = return_add(16, 100)
print(addition)


# Multiplication with return
def multiply(num1, num2):
    return num1 * num2


a = multiply(15, 20)
b = 15
print(a + b)


# Challenge
# Create a function to check if a number is even
# Use return

def even_check(number):
    return number % 2 == 0


print(even_check(16))
print(even_check(15))


# Create a function to check if any number in a list is even
# Use Return
def even_check_list(number_list):
    for i in number_list:  # Iterate through each number
        if i % 2 == 0:
            print(i, "is Even")
        else:
            print(i, "is Odd")


lst = [1, 2, 3, 4, 5, 6, 7]
even_check_list(lst)


# Whenever I find an even number in a list return True
def even_check_list2(lst):
    for i in lst:
        if i % 2 == 0:
            return True
    return False


print(even_check_list2(lst))

lst2 = [1, 3, 5]
print(even_check_list2(lst2))
