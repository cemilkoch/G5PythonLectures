# Concatenation
# String concatenation means adding strings together
# The + operator concatenates only Strings

s = "Apple"
t = "iPhone"
u = "11 Pro"

# Without Whitespace
print(s + t + u)

# With Whitespace
print(s + " " + t + " " + u)

# Also Use comma(,) to concatenate strings
print(s, t, u)

# The * operator will print multiple copies of a string
name = "Cemil"
print(name * 6)
print((name + " ") * 6)

# The number can be negative or zero. But it will not print negative or zero
# It will print empty string
print(name * -7)
print("Name * -8" + name * -8)

str1 = "I love programming with"
str2 = "Python"

print(str1, str2)

# STRING METHODS
str3 = "I am learning Python and Java"
str4 = "capitalize me"
str5 = "capitalize all the words"

# upper() method
print(str3.upper())

# lower() method
print(str3.lower())

# capitalize() method
print(str4.capitalize())

# title() method
print(str5.title())

# split() breaks the string at the separator and returns a list of string
print(str3.split())

str6 = "Python, Java, C++, ...."
print(str6.split(","))

# .format()
# {} = placeholders
print("Insert another string with curly brackets: {}".format("The inserted String"))
print("My name is {0} and my last name is {1}".format("Cemil", "Koc"))

name = "Michael"
last_name = "Johnson"
print("His name is {} and his last name is {}".format(name, last_name))

print("\n*****************\n")

# Placeholder method %s Python 2.7
print("I am going to insert %s here." % ("something"))
print("I am going to insert %s text, and %s text here." % ("some", "more"))

x, y = 'some', 'more'
print("I am going to insert %s text, and %s text here." % (x, y))

# Format Conversion methods
# %d it is used for integers
print("I wrote %d lines of code today" % 70)

# %f it is used for floating numbers
print("Floating point numbers: %0.5f" % 3.14151617)

# f string formatting
name2 = "Cemil"
last_name2 = "Koc"
print(f"My name is {name2} and my last name is {last_name2}")
