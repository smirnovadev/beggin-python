# Python string examples - all assignments are identical.
String_var = 'Python'
String_var = "Python"
String_var = """Python"""

# with Triple quotes Strings can extend to multiple lines
String_var = """ This document will help you to
explore all the concepts
of Python Strings!!! """

# Replace "document" with "tutorial" and store in another variable
substr_var = String_var.replace("document", "tutorial")
print (substr_var)

sample_str = 'Python String'

print (sample_str[0])       # return 1st character
# output: P

print (sample_str[-1])      # return last character
# output: g

print (sample_str[-2])      # return last second character
# output: n

## COMMON ERRORS
sample_str = "Python Supports Machine Learning."
print (sample_str[1024])      #index must be in range

# IndexError: string index out of range

sample_str = "Welcome post"
print (sample_str[1.25])      #index must be an integer

# TypeError: string indices must be integers
