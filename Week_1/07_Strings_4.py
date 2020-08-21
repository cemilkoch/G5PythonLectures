# The strip() method removes any whitespace from the beginning or the end:
name = "    Cemil Koc    "
print(name.strip())
print(len(name))

# replace() method replaces a string with another string
a = "Hello Python"
print(a.replace("Python", "Java"))
print(a)

# Strings are immutable == You can't modify a string

# The split method splits into substrings
text = "Python Language"
print(text.split(" "))

# Challenge | Split the email address by the @ symbol
prof_address = "michael@nyu.edu"
print(prof_address.split("@"))

print("\n*************\n")

# sep, end
# The print function uses sep to separate arguments and end after the last parameter
print("I love programming in Python", "Java", "SQL", sep=", ", end="!\n")

print('C', 'O', 'D', 'E', sep=" ")
print('08', '20', '2020', sep='/')
print('cemil','gmail.com', sep="@")

