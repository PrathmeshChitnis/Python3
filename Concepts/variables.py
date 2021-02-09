""" Type casting """

var1 = "54"
var2 = "36"

print("This is the normal print for strings")
print(var1 + var2)

print("The are type cased string to integer")
print(int(var1) + int(var2))

print(100 * (int(var1) + int(var2)))

"""Complex type casting from string to int to string """

print(100 * str(int(var1) + int(var2)))

"""  inputs  """

number = input("Enter your number which is to be added to 10")
print ("The number plus 10 is :- ", int(number) + 10)