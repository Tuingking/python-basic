from os import path

# r in front used for read "/""
strPath = r"D:/coding/python"

print("The current directory is: {}".format(path.curdir))
print("abspath: {}".format(path.abspath(path.curdir)))
print("dirname: {}".format(path.dirname(path.curdir)))
print("basename: {}".format(path.basename(path.curdir)))
print("exists: {}".format(path.exists(path.curdir)))
print("isdir: {}".format(path.isdir(path.curdir)))
print("isfile: {}".format(path.isfile(path.curdir)))
print("\n")
print("The current directory is: {}".format(strPath))
print("abspath: {}".format(path.abspath(strPath)))
print("dirname: {}".format(path.dirname(strPath)))
print("basename: {}".format(path.basename(strPath)))
print("exists: {}".format(path.exists(strPath)))
print("isdir: {}".format(path.isdir(strPath)))
print("isfile: {}".format(path.isfile(strPath)))
