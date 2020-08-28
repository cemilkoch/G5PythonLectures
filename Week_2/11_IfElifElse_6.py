# Username and password example
# usernames = ["Bill", "Steve", "Michael", "Cemil"]
# passwords = ["123456", "12345", "1234", "123"]
#
# username = input("Please enter your username ")
# password = input("Please enter your password ")
#
# if username in usernames:  # If username is inside usernames list
#     if password in passwords:
#         print("Access granted")
#     else:
#         print("Incorrect password")
# else:
#     print("Incorrect username")

allowed_users = {'Bill': '123456', 'Steve': '12345', 'Michael': '1234567', 'Cemil': '123'}
username = input("Please enter your username ")
password = input("Please enter your password ")

# dictionaryName[keyName] will return value

if username in allowed_users:
    if password == allowed_users[username]:
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")
