# this shows how to read a file from you py prog

my_filename = "for.py"

with open(my_filename) as f:
    content = f.readlines()

for lines in content:
    print(lines),