"""
Problem - 
Challenge: Write a function name_swap(name_string) that converts an input string name_string
of the form "first last" into the form "Last First" and returns this converted string. 
For this problem, you may assume that name_string contains exactly one space.
"""

"""
Solution - Function that swaps and capitalizes first and last names
"""


def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    (first, last) = name_string.split(" ")
    return last.capitalize() + " " + first.capitalize()
    
# Tests

print(name_swap("joe warren"))
print(name_swap("scott rixner"))
print(name_swap("john greiner"))


# Output

#Warren Joe
#Rixner Scott
#Greiner John