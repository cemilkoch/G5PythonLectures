"""
Write a function that asks the user to enter a distance in miles,
then convert that distance to kilometers and print it out. The conversion formula is as follows:
1 Miles = 1.60934 Kilometers
"""


def miles_km():
    miles = float(input("Enter miles: "))
    km = miles * 1.60934
    print(miles, "miles is", km, "kilometers")


"""
Write a function which will find all such numbers which are divisible 
by 3 but are not a multiple of 5, between 500 and 1200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line. 
"""


def func():
    for i in range(500, 1201):
        if i % 3 == 0 and i % 5 != 0:
            print(i, end=', ')


func()

"""
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), 
it should give the driver one demerit point and print the total number of demerit points. 
For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”

"""

print()


def speed_checker(speed):
    if speed < 70:
        print("Ok")
    else:
        points = (speed - 70) // 5
        if points <= 12:
            print("Points", points)
        else:
            print("License suspended")


speed_checker(120)
