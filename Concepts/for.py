# simple for loop with list

friuts = ["apple", 'banana', "orange"]

for f in friuts:
    print(f)

# simple for loop with string

print("----------------------------------")

name = "Alexander"

for N in name:
    print(N)

# break statement with for loop

print ("----------------------------------")

names = ['Sam','John','Max','Jill']

for Name in names:
    print(Name)
    if Name == 'Max':
        break

# continue statement with for loop

print("----------------------------------")

fruits = ["Apple", "Mango", "Orange"]

for f in fruits:
    if f == "Mango":
        continue
    print(f)

# simple range () in for loop

print("----------------------------------")


for i in range(6):
    print(i)

# range () with two para prints the range between the two para's

print("----------------------------------")

for i in range (2,7):
    print(i)

# range() with three para (x,x,y) here y is the value to be incremented

print("----------------------------------")

for i in range(0,10,2):
    print(i)

# else in for loop

print("----------------------------------")

for i in range(10):
    print(i)
else:
    print("The printing for the loop is completed no more items to print")

# nested for loop
# printing each adjective for every fruit

print("----------------------------------")

fruit = ["apple", "mango", "orange"]
adj = ["red", "yellow", "bright"]
for x in fruit:
    for y in adj:
        print(x,y)

# loops cannot be kept empty use pass to avoid errors

print("----------------------------------")

i = 0
for i in range(0,10):
    pass