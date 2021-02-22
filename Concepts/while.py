# while loop simple programs

i = 1
while i < 6:
    print(i)
    i += 1


# break statement

print ("----------------------------------")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue statement

print ("----------------------------------")

i = 0
while i < 6:
    i += 1
    if i ==3: # it will skip 3 and not print it because of the continue statement
        continue
    print(i)

# the else statement

print ("----------------------------------")

i = 0
while i <= 6:
    print(i)
    i += 1
else:
    print("i is not less the 6 any more")
