"""
Ask the user for their name and state.
Your application should print what region the user lives in.
Region 1: Northeast
Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, and Vermont
New Jersey, New York, and Pennsylvania
Region 2: Midwest
Illinois, Indiana, Michigan, Ohio, and Wisconsin
Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, and South Dakota
Region 3: South
Delaware, Florida, Georgia, Maryland, North Carolina, South Carolina,
Virginia, District of Columbia, and West Virginia Alabama, Kentucky,
Mississippi, and Tennessee Arkansas, Louisiana, Oklahoma, and Texas
Region 4: West
Arizona, Colorado, Idaho, Montana, Nevada, New Mexico, Utah, and Wyoming
Alaska, California, Hawaii, Oregon, and Washington
Example:
Input:
Name - Selim Region - New Jersey

Output:
Selim, you live in North East
"""

name = input("Name - ")
state = input("State - ").title()

northeast = ["Connecticut", "Maine", "Massachusetts", "New Hampshire", "Rhode Island", "Vermont",
             "New Jersey", "New York",
             "Pennsylvania"]
midwest = ["Illinois", "Indiana", "Michigan", "Ohio", "Wisconsin",
           "Iowa", "Kansas", "Minnesota", "Missouri", "Nebraska",
           "North Dakota", "South Dakota"]
south = ["Delaware", "Florida", "Georgia", "Maryland", "North Carolina", "South Carolina",
         "Virginia", "District of Columbia", "West Virginia", "Alabama", "Kentucky",
         "Mississippi", "Tennessee", "Arkansas", "Louisiana", "Oklahoma", "Texas"]
west_str = "Arizona, Colorado, Idaho, Montana, Nevada, New Mexico, Utah, Wyoming, " \
       "Alaska, California, Hawaii, Oregon, Washington"
west = west_str.split(",")

location = ""  # This variable will be assigned depending on the user input
if state in northeast:
    location = "North East"
elif state in midwest:
    location = "Mid West"
elif state in south:
    location = "South"
elif state in west:
    location = "West"
else:
    location = "Unknown"

print(f"{name} you live in {location}")

