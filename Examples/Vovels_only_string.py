#print vowels from a give string

mystr = input("Enter a String ")
myvov = ""

for char in mystr:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
        myvov += char

print(myvov)