# immutable elements
# We use parantheses to create a tuple
# Once we create a tuple, we can't modify tuple

# Empty Tuple
tuple_1 = ()
print(type(tuple_1))
print(tuple_1)

# Tuple having number
tuple_2 = (1, 2, 3, 4, 3.14)
print(type(tuple_2))
print(tuple_2)

# Tuple with mixed data types
tuple_3 = (1, 2, 3, "Hello", 2.1)
print(tuple_3)

# Nested tuples
tuple_4 = ("Lion", [1, 2, 3], (2.14, 3, 14), True)
print(tuple_4)

# Creating a tuple with a single element
tuple_5 = ("Python")  # str
print(type(tuple_5))

# Tuple with a single comma
tuple_6 = ("python",)
print(type(tuple_6))

# By convention you need to add parantheses
tuple_7 = "cemil", "python", 2, 3  # not a good usage
print(type(tuple_7))

