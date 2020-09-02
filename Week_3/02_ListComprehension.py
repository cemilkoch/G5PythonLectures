list1 = [1, 2, 3, 4, 5]

print(list1)

list2 = []

for i in list1:
    list2.append(i)

print("list2", list2)

# Using List Comprehension
# list1 = [1, 2, 3, 4, 5]
list3 = [var for var in list1]
print("list3", list3)

squares = [i ** 2 for i in list1]
print("Squares", squares)

numbers = list(range(51))
# even_numbers = []
# for i in numbers:
#     if i % 2 == 0:
#         even_numbers.append(i)

even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)

word = 'Python'
# letters = []
# for i in word:
#     letters.append(i)
# print(letters)
letters = [i for i in word]
print(letters)


