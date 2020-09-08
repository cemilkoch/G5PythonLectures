# Create a function to find out the words that begin with vowels
# a, e, i, o, u
def check_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in words:
        if i[0] in vowels:
            print(i)


lst = ['banana', 'oranges', 'apples', 'melons']


# check_vowels(lst)


# With Return
def check_vowels2(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lst = []
    for i in words:
        if i[0] in vowels:
            lst.append(i)
    return lst

print(check_vowels2(lst))