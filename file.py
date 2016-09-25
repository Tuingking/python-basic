import os

''' File
=========================================================================================================
wb  = create file and write
ab+ = read & append
'''
# Create and write file
test_file = open("test.txt","wb")
print (test_file.mode) # wb
print (test_file.name) # test.txt

test_file.write(bytes("Write me to the file", 'UTF-8'))
test_file.close()

# Read File
test_file = open("test.txt","r+")
text_in_file = test_file.read()
print (text_in_file)

# Remove file
# os.remove("test.txt")