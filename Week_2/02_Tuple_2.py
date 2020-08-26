# Accessing elements within a tuple
my_tuple = ("J", 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't')

# We need to use index numbers to access elements
print(my_tuple[0])
print(my_tuple[-1])

# Tuples are IMMUTABLE, they can't be changed
# Lists are MUTABLE, they can be changed

# Once you create a tuple, you can't change it
my_tuple_2 = (4, 5, 6, 7)
# my_tuple_2[0] = 15 does not support item assignment

# del my_tuple_2[3] does not support item deletion

# You can delete tuples completely, but you can't delete an item from a tuple
# del my_tuple_2
print(my_tuple_2)

# Movie release years
movie_years = (2007, 2002, 2003)

# Tuple Membership Test
my_tuple_3 = ('P', 'y', 't', 'h', 'o', 'n')

# In keyword
print('y' in my_tuple_3)

# Not in keyword
print('n' not in my_tuple_3)

# If you use tuples you can create data that will not change
# this will guarantee that data is going to protected

