# *args == non keyword arguments

def print_scores(student, *scores):
    print("Student name:", student)
    print(type(scores))
    for score in scores:
        print(score)


print_scores("Navin", 100, 50, 90, 80, 70)


# **kwargs == keyword arguments
# ** asterisk allows the parameters to be entered as a dict format

def print_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)


# k_name=value
print_kwargs(k1=1, k2=2, k3=3, k4=4, k5=5)


# items() method
def print_names(**names):
    for k, v in names.items():
        print(f"The value of {k} is {v}")


print_names(FirstName='Cemil', SecondName='Ahmet', ThirdName='Selim')


def print_pet_names(owner, **kwargs):
    print("Owner name", owner)
    for k, v in kwargs.items():
        print(k, ":", v)


print()
print_pet_names("Priya", dog='Max', fish=['Nemo', 'Dorry', 'Curly'], turtle="Speedy")

print()


# *args and **kwargs used together
def student_information(*args, **kwargs):
    print(args)
    print(kwargs)


classes = ('Marketing', 'Data Mining')
information = {'name': 'Cemil', 'last': 'Koc', 'age': 25}

student_information(*classes, **information)
