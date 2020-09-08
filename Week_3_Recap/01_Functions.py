# 1-) def == define a function
# 2-) function_name
# 3-) parameters
# 4-) body

# A function is a sequence of instructions with a name

# Create a function to find the volume of a cube
# v = a^3

def cube_volume(side_length):
    volume = side_length ** 3
    return volume


result1 = cube_volume(2)
result2 = cube_volume(10)
print("A cube with side length of 2 has a volume of", result1)
print("A cube with side length of 10 has a volume of", result2)

# Calling the function with the user input
side_length = int(input("Enter a side length: "))
result3 = cube_volume(side_length)
print("A cube with side length of", side_length, "has a volume of", result3)
