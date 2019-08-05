"""
Strings and collections

A String is a immutable sequence of Unicode code-points
"""

print('This is a string')
print("This is a string too")
# Concatenation and adjacent strings
s1 = "First"
s2 = "Second"
print(s1 + " " + s2)
#multi-line String and newlines
s3 = """
This is 
a multi-line
string
"""
print(s3)
s4 = "This is \na multi-line \nstring"
print(s4)
#Support for backslash
s5 = "A \\ in a string"
print(s5)
#Raw strings
raw_string = r"C:\User\Document\Books"
print(raw_string)

#String as sequence
s =  "parrot"
print("s[4]", s[4], type(s))

s = s.title()
print(s)