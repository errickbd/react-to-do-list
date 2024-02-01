# Intro to Python
import os

# Dynamically typed
# First class functions - functions can be assigned to variables or passed
# as an argument to another function (higher order function)
# Neither need to have a separate compilation step

# Primitive types

# Number
# Integer type
a_small_number = 4
# print(type(a_small_number))

# Float type
a_decimal_number = 3.7
# print(type(a_decimal_number))

# Strings

a_string = 'hello world'
another_string = "welcome to the internet"
# print(type(a_string))
# print(type(another_string))

# String interpolation with f string
day = 'Friday'
activity = 'bowling'
# print(f"Let's go {activity} on {day} afternoon.")
another_f_string = f"Let's go {activity} on {day} afternoon!!!!"
# print(another_f_string)

# Booleans
something_true = True
something_false = False
# print(type(something_true))
# print(something_false)

"""
Non Primitive Types
Lists and Dictinaries are awesome in python
"""

# Lists
berries = ['grape', 'tomato', 'cucumber', 'eggplant', 'banana', 'watermelon', 'pumpkin']
print(type(berries))

# print(berries[1])
# print(berries[-1])
# print(berries[0:3]) #slice from 0 to index 3
# print(berries[2:4]) # cucumber, eggplant
# print(berries[2:]) # slice all the way to the end
# print(berries) # original list untouched, slicing is nondestructive

# Tuple
# Tuples are immutable - they're not meant to be changed once you create them.
days_of_the_week = ('sunday', 'monday', 'tuesday','wednesday','thursday', 'friday')
# print(type(days_of_the_week))
# print(days_of_the_week)

# print(days_of_the_week[4])

# Dictionaries
jeff = {
    'name': 'jeff',
    'age': 44,
    'job': 'influencer'
}

# print(jeff['age'])

people = [
    {
        'name': 'jeff',
        'age': 44,
        'job': 'influencer',
    },
    {
        'name': 'alice',
        'age': 44,
        'job': 'influencer',
    },
    {
        'name': 'carol',
        'age': 65,
        'job': 'life coach',
    },
]

# print(people[1]['name'])

# Functions

def gimme_five():
    return 5

# print(gimme_five())

def add_one(n):
    return n + 1

# print(add_one(10))

def describe_berries(n, color):
    print(f"I have {n} {color} berries")

# describe_berries(2, "blue")

def describe_berries_again(n=1, color="blue"):
    print(f"I have {n} {color} berries")

# describe_berries_again()
# describe_berries_again(color='red')
# describe_berries_again(color='red', n=3)

# *args for unspecified number of params
def print_them_all(*args):
    print(type(args))
    print(args)

# print_them_all("hello", "world", "sunday", "blue", "monday", "new", "order")

# **kwargs
def who_am_i(**kwargs):
    for k in kwargs:
        print(f'My {k} is {kwargs[k]}')

# who_am_i(name='Dan', age=20, job='skydiver')

# If else statements

def can_drink_beer(age, country):
    if age >= 21 or age >= 18 and country == 'Canada':
        return True
    # else if
    elif country == 'Antarctica':
        return True
    else:
        return False

# print(can_drink_beer(20, 'USA'))
# print(can_drink_beer(21, 'USA'))
# print(can_drink_beer(18, 'Canada'))
# print(can_drink_beer(4, 'Antarctica'))

# For loops

my_list = ["a", "b", "c"]

# for x in my_list:
    # print(x)

# for i, x in enumerate(my_list):
    # print(i, x)

# range
# for x in range(10):
#     print(x)

# loop thru dictionaries

my_dict = {
    "donuts": "yummy",
    "green bean": "gross",
}

# loop thru dict keys
# for k in my_dict:
#     print(k)
#     print(my_dict[k])

# for v in my_dict.values():
#     print(v)

# While loops
# x = 9
# while x > 0:
#     print(x)
#     x = x - 1

# File paths

os.getcwd()
# print(os.getcwd())

# print(os.path.abspath('.'))

# Reading and writing files

# Using a relative path
# with open('./example.txt', 'r') as file:
#     for line in file:
#         print(line)

abs_path = os.path.abspath('./example.txt')
# print(abs_path)

# with open(abs_path, 'r') as file:
#     for line in file:
#         print(line)

# Dictionary zip()


numbers = [1,2,3]
letters = ['a', 'b', 'c']

zipped = zip(numbers, letters)

print(letters)

print(zipped)
print(list(zip(numbers, letters)))
print(dict(zip(numbers, letters)))