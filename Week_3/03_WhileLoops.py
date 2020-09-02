# while condition: condition = Boolean == True or False
#   body
#   statement2
#   etc.

# If true then the statements will execute
# If false then statements will not execute

# Print the numbers from 0 to 10
i = 0
while i <= 10:
    print('i value', i)
    i = i + 1

# print numbers from 0 to 20 increase them by 2
m = 0
while m <= 20:
    print(m)
    m = m + 2

# Infinite Loop
# while True:
#     print(10)

# Printing Python 5 times
n = 0
while n < 10:
    print("Python")
    n = n + 2

print("\n***************\n")
x = 0
while x < 10:
    print("x is currently :", x)
    print("x is still less than 10, adding 1 to x")
    x = x + 1

print("\n***************\n")

x = 10
while x >= 0:
    print("x is", x)
    x = x - 1
else:
    print("All done!")

# break
# continue
# break : breaks out of the loop exits completely
# continue: skips the remaining statements and goes to the top
# of the loop

t = 0

while t < 10:
    print("t value", t)
    t = t + 1
    if t == 5:
        break
    else:
        print("continuing")
        continue



