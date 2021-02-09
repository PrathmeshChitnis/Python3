# String, String slicing and other functions in python 3

mystr = "Hello this is string"

print(mystr)

# string slicing

print(mystr[4])
print(mystr[:0])
print(mystr[:5])

# printing part of a string

print(mystr[0:5])

# lenght calculation of a string using len

print(len(mystr))

# string slicing using range [::this] - extended slice

print(mystr[0:5:2])

# with negative index


print(mystr[-4:])
print(mystr[-1:0])

# extended negative slice

print(mystr[::-1])  # a naive way to reverse the string not recommended

print(mystr[::-2])

""" String functions 
    :type - use in type casting
    isalnum - alphanumeric [T/F]
    isalpha - alphabetic [T/F]
    endswith - checks the end of the string compares and returns [T/F]
    count - counts the letters in one string
    capitalize - first letter of the string is converted changed to capital 
    find - find any word in the string [gives the starting of the index to be found]
    lower - converts into lowercase
    upper - converts into uppercase
    replace - (,) takes to params replaces the first one with the second param
    
    """
