a_string = "Hello String"
b_string = 'Hello Python'
c_string = """This is a string as well"""
d_string = '''This is also a string'''

print(a_string)
print(b_string)
print(c_string)
print(d_string)

text = "The rain in New York stays mainly in the plain."
x = "New York" in text
print(x)

y = "New Jersey" not in text  # Not inside the text
print(y)

# Challenge | Write a program to check if letter 'e' is present in word chicken
print("e" in "chicken")

# To create a multiline string use """ """"
multiline_str = """We can print
multiline string 
by using triple quotes"""
print(multiline_str)

# join method joins list items that are separated
lst = ["This", "is", "a", "list", "of", "items", "that", "are", "split"]
string = ' '.join(lst)
print(string)

# Challenge | join the numbers with a dot(.)
a = ['192', '168', '1', '3']
b = '.'
c = b.join(a)

print(c)

# count() method
astring = "Hello World!"
print(astring.count("l"))
