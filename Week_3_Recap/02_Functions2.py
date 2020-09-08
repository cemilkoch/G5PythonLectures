# Calling cube_volume() inside the main() function
def main():
    # Assigning function cube_volume() to result
    result = cube_volume(3)
    print("A cube with side length 3 has a volume of", result)


# Creating a function to calculate a volume
def cube_volume(side_length):
    return side_length ** 3


# Calling the main() function
main()

