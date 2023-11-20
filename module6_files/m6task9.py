""" 
There are 2 records in different unicodes utf-8 and utf-16. 
It is needed to define if these records are equal to each other.

Implement function is_equal_string(utf8_string, utf16_string) that returns True if 
the records are equal and False if they are not equal
"""

def is_equal_string(utf8_string, utf16_string):
    return utf16_string.decode('utf-16').casefold() == utf8_string.decode('utf-8').casefold()

s1 = "Hello!"
s2 = "Prints###"

utf8_1 = s1.encode('utf-8')
utf16_1 = s1.encode('utf-16')
utf_16_2 = s2.encode('utf-16')

#print(type(utf8_1))

print(is_equal_string(utf8_1, utf16_1))
print(is_equal_string(utf8_1, utf_16_2))
