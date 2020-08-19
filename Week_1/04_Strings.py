# A string is a sequence of characters
# A character is simply a symbol
# To create a String in python we use '' or ""

print(type("Silicone Labs"))
print('Hello')

name = 'Cemil'
print(name)

text = "I'm a programmer"
print(text)

text2 = 'I\'m a programmer'  # \' to create a single quote
print(text2)

text3 = "Use \nto print new line"  # \n creates a newline
print(text3)

s = "Hello World"
# variableName[indexNumber]
print(s[0])  # H
print(s[6])  # W

# VariableName[start:end]
# Retrieve Hello
print(s[0:5])
print(s[:5])

# Retrieve World
print(s[6:])
print(s[6:11])

# a[start:stop] items start through stop-1
# a[start:] items start through the rest of the string
# a[:stop] items from the beginning through stop-1
# a[:] a copy of the string

print(s[:])

# Step Point
# variable[start:end:step point]
# Hello World
print(s[0:11:2])  # HloWrd
print(s[::3])  # HlWl

# Retrieve Wr
print(s[6:9:2])

# Retrieve Wrd
print(s[6:11:2])

# In Python ending characters start from negative 1(-1)
str2 = "Java"
print(str2[-1])

# print v
print(str2[-2])
print(str2[2])

# Reversing a string in Python
print(str2[::-1])





