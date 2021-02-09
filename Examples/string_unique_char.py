#Take one string and get the unique char


mystring = input("Please enter a string ")
mystring2 = ""

mystring = mystring.lower()
for char in mystring:
    if char not in mystring2:
        mystring2 += char



print(mystring2)









