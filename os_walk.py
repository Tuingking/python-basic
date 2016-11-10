import os

spath = r"D:/coding/python"

# Everything
print(os.listdir(spath))
print("\n")
# # Get everything split
# for roots, dirs, files in os.walk(spath):
#     for dir in dirs:
#         print("Dir: {}".format(dir))
#     for file in files:
#         print("File = %s" %file)

# Only the roots
roots = next(os.walk(spath))
print("Roots = %s" % roots[0])
print("Dirs = %s" % roots[1])
print("Files = %s" % roots[2])

# Only the dir