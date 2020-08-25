# Lists are created using []
l = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# len()
print(len(l))

# min() method returns the lowest number
print(min(l))

# max() method returns the highest number
print(max(l))

# adding elements to list
print(l + [100, 110, 120])

# List Slicing
b = [0, 5, 11, 22, 33, 44, 77, 88, 99]

# Syntax of Slicing b[x:y:z]
print(b[0:7:1])  # elements from 0(included) to 7(excluded)
print(b[0:7:2])

# if z is not given, z is 1 by default
print(b[0:7])

# if z is positive, slicing will be from left to right,
# so x should be less than y
print(b[2:7:1])

# if z is negative, slicing will be from right to left,
# so x should be greater than y
print(b[7:2:-1])

# Reverse method will reverse the list
b.reverse()
print(b)

b.reverse()
print(b)
