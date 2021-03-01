# over writting a file

filename = "Hack2.py"
# givening the new file name above

myfile = open(filename, 'w')
# opening the file with w as the write permissions

myfile.write("This was overwritten by python")
# writing the file

myfile.close()
#closing the file


# you can also append to a file doing following

myfile = open(filename, 'a')  # a stands for appending the file

myfile.write("\n This test was appened using python")

myfile.close()
