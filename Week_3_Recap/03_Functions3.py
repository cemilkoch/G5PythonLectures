# The return keyword is used to specify the result of a function
# When the return keyword is processed, the function will exit

def cube_volume(length):
    return length ** 3


def cube_volume2(length):
    if length >= 0:
        return length ** 3
    else:
        return 0


def cube_volume3(length):
    if length >= 0:
        volume = length ** 3
    else:
        volume = 0
    return volume


result = cube_volume3(10)
print("The volume of side length of 10 is", result)





