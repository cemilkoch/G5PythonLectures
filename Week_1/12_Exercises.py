"""
Imagine that you are given 2 strings(string1 and string2).
Assume that the number of characters in each string is an odd number.
Make an application that returns a new string made of the first, middle,
and the last character of string1 concatenated with the first, middle, and last character of string2.

Example:
string1 = "Butterfly" len() = odd
string2 = "Koala"

Output:
BeyKaa
"""

string1 = "Butterfly"
string2 = "Koala"

print(string1[0] + string1[len(string1) // 2] + string1[-1]
      + string2[0] + string2[len(string2) // 2] + string2[-1])

'''
Make a program that receives a string input from the user, and then prints out
the first two letters twice with an ellipsis ... 
and space after each, and then the full string with a question mark at the end.
Example:
Input:
magician

Output:
ma.. ma.. magician?
---------------

Input:
amazing
Output:
am.. am.. amazing?
'''

word = input("Please enter a word: ")
print((word[0:2] + ".. ") * 2 + word + "?")

"""
Write code so it takes a base input and a height input of a triangle from the
user and then prints the area of the triangle.
Area = (base * height) / 2
"""
base = int(input("Enter base: "))
height = int(input("Enter height: "))
print("Area", base * height / 2)

"""
Write a program that asks the user for a,b,c: each a unique string and x: an integer. 
Print out the number that is returned after the sum of the lengths of all the strings is divided by x.
Example:
Input:
    elephant
    tooth
    joke
    5
Output:
    3.4
"""

a = input("1.) ")
b = input("2.) ")
c = input("3.) ")
x = int(input("Number: "))
print((len(a) + len(b) + len(c)) / x)

