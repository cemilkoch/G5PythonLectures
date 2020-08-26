# Dictionary can be created using curly brackets {}
# In dictionary an item has a key and a value that is
# expressed as a pair {key: value}
# Each key and value is separated by a colon(:)

# Lists [], tuples (,), dictionaries {}


# Creating a dictionary {}
dictionary = {}
print(type(dictionary))
print(dictionary)

# Creating a dictionary with integer keys {keys: value}
dictionary_2 = {1: "apple", 2: "banana", 3: "pear"}

# Creating a dictionary with mixed data types
dictionary_3 = {'name': 'Cemil', 2: [10, 20, 30]}

# Creating a dictionary using dict()
dictionary_4 = dict({1: 'apple', 2: 'banana'})

personal_details = {'name': 'Cemil', 'last_name': 'Koc', 'age': 25}

# Dictionaries are unordered, you can get using a key

# Accessing elements inside dictionaries
# [] and get() method is used to retrieve elements
# []
print(personal_details['name'])

# get()
print(personal_details.get('last_name'))

# Changing elements of a dictionary
personal_details['age'] = 26
print(personal_details)

# Adding elements to a dictionary
personal_details['address'] = 'New Jersey'
print(personal_details)

# Removing elements from a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# pop() is removing an item with the given key
squares.pop(4)
print(squares)

# popitem() removes an arbitrary item, last item
squares.popitem()
print(squares)

# clear()
squares.clear()
print(squares)



