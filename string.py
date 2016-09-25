''' String
=========================================================================================================
'''
# PART 1
print("PART 1")
print("="*10)
quote = "\"Always remember you are unique"
multi_line_quote = '''  just
like everyone else
'''
print ("%s %s %s" % ("I like the quote", quote, multi_line_quote))
# Return:
# I like the quote "Always remember you are unique   just
# like everyone else

# PART 2
print("PART 2")
print("="*10)
long_string = "Hello World My Friends "
print ("long_string = %s\n" % long_string)
print ("long_string[:-3] = %s" % long_string[:-3]) # "Hello World My Frien"
print ("long_string[-3:] = %s" % long_string[-3:]) # ds
print ("long_string[:3] = %s" % long_string[:3]) # Hel
print ("long_string.find('my') = %s" % long_string.find("my")) # -1
print ("long_string.find('My') = %s" % long_string.find("My")) # 12
print ("long_string.strip = %s" % long_string.strip()) # "Hello World My Friends"
print ("long_string.split = %s" % long_string.split()) # ['Hello', 'World', 'My', 'Friends']


print ("I don't like ", end="")
print ("newlines")