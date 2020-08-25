# An escape character is a backslash \ followed by the character you want to insert

# text = "We are the so-called "Vikings" from the north."

text = "We are the so-called \"Vikings\" from the north."
print(text)

# \'
text2 = 'It\'s alright'
print(text2)

# \\
text3 = "This will insert one \\ (backslash)"
print(text3)
print("This will print 3 \\\\\\")

# \n creates new line
text4 = "Hello\nPython"
print(text4)

# \t tab == creates 4 spaces
text5 = "Hello\tWorld"
print(text5)

# \b backspace is going to delete one character
text6 = "Hello\bWorld"
print(text6)

# Raw Strings
# use r before your string to change it to a raw string
# Every character you add into a raw string stays the way you wrote it
# It prints exactly the same way you wrote it
print("C:\\ProgramFiles")
print(r"C:\\nProgramFiles")
