# Challenge
# Get a name from the user
# If the name is Max or John or Eli greet them with a Welcome message
# if the name is different than those above print "the name is invalid"

name = input("Enter a name: ")
name_list = ["Max", "John", "Eli"]

# 1st Solution
# if name.capitalize() in name_list:
#     print("Welcome", name)
# else:
#     print("The name is invalid")

# 2nd Solution
name = name.lower()
if name == "max" or name == "john" or name == "eli":
    print("Welcome", name)
else:
    print("The name is invalid")
