# Condition1
# Condition2

# if condition1:
#   Execute when condition1 is true
#   if condition2:
#       Execute when condition2 is true
#   if block will end here

x = 10  # Condition1 = x == 10
# Condition2 = x < 20
if x == 10:
    if x < 20:
        print(x, "is less than 20")
    else:
        print(x, "is greater than 20")

# Ask the user for a time number in 24hr format 0 - 23
# If the time is before 10 print good morning
# If time is after 10 and before 12 print soon time for a lunch
# If time is after 12 and before 18 print good day
# If time is after 18 and before 22 print Good evening
# If time is after 22 print good night

time = int(input("Please enter a time "))
if 0 <= time < 24:
    if time <= 10:
        print("Good morning")
    elif 10 < time <= 12:
        print("Soon time for a lunch")
    elif 12 < time <= 18:
        print("Good day")
    elif 18 < time <= 22:
        print("Good evening")
    else:
        print("Good night")
else:
    print("Please enter a correct time")
