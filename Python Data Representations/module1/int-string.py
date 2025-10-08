"""
Problem - 
Write a function make_int(int_string) that takes as input the string int_string and checks whether
int_string can be converted to a non-negative integer.  If so, the function returns that integer. 
Otherwise, the function returns the integer -1. For this question, be sure to use the Python 
docs to search for a string function that checks whether a string consists entirely of digits.
"""

"""
Solution - Function that checks whether a string can be converted to an integer
"""


def make_int(int_string):
    """
    Given the string int_string, return the associated integer if all 
    digits are decimal digits.  Other return -1.
    """
    
    if int_string.isdigit():
        return int(int_string)
    else:
        return -1
    
# Test

print(make_int("123"))
print(make_int("00123"))
print(make_int("1.23"))
print(make_int("-123"))


# Output

#123
#123
#-1
#-1