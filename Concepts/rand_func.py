# Random function use-case



# printing random numbers

from random import *

print(randint(1, 100))    # prints a single random number between 1 to 100

# sffuling the give list

print("\t------------------")

list_of_numbers = ['1', '2', '45', '46', '67', '889']
shuffle(list_of_numbers)
print(list_of_numbers)

# picking random items from the list

print("\t------------------")
list_of_numbers = ['1', '2', '45', '46', '67', '889']
x = sample(list_of_numbers,4)   # list name, no of items from the list to be picked
print(x)

# picking random items from the list of strings

print("\t------------------")

list_of_fruits = ['Apple', 'Banana', 'Orange', 'Watermelon', 'Grapes', 'Pineapple']
print(sample(list_of_fruits, 3))


