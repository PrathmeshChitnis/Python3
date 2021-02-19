# Python 3 dictionary explained


my_dict = {
    "name": "YYYY",
    "Lastname": "XXXX",
    "Number": "xxx-xxx-xxxxx"
}

print(my_dict)

# Accessing items in a dictionary using get()

print("--------------------------")

my_dict = {
    "name": "YYYY",
    "Lastname": "XXXX",
    "Number": "xxx-xxx-xxxxx"
}

x = my_dict.get("Lastname")
print(x)

# to get all the keys of the dictionary key() methood

print("--------------------------")

my_dict = {
    "name": "YYYY",
    "Lastname": "XXXX",
    "Number": "xxx-xxx-xxxxx"
}

get_keys = my_dict.keys()
print(get_keys)

# to get all the Values of the dictionary values() method

print("--------------------------")

my_dict = {
    "name": "YYYY",
    "Lastname": "XXXX",
    "Number": "xxx-xxx-xxxxx",
    "Class": "4A"
}

get_values = my_dict.values()
print(get_values)

# to get each item in the dictionary items() methood

print("--------------------------")

my_dict = {
    "name": "YYYY",
    "Lastname": "XXXX",
    "Number": "xxx-xxx-xxxxx"
}

get_items = my_dict.items()  # returns a key:value pair as a tupple
print(get_items)

# changing values for a key in dictinory

print("--------------------------")

dict_change = {
                "model" : "Pagani",
                "Name" : "Hyura",
                "Make" : "2020"
}

change = dict_change.get("Make")
print("The model for the hyper car is of ", change)

change = dict_change["Make"] = "2021"
print("The model is now upgraded to :-",change)

# changing values using the update() method

print("--------------------------")

dict_change = {
                "model" : "Pagani",
                "Name" : "Hyura",
                "Make" : "2020"
}

dict_change.update( {"Make" : "2021"})
print(dict_change)

# adding items to a dictionary




