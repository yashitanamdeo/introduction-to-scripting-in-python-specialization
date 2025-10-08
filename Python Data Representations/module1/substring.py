"""
Problem - 
Write a function is_substring(example_string, test_string) that takes the strings example_string and
test_string and returns True if there exists a slice of example_string that exactly equals test_string
and returns False otherwise. Note that the body of this function requires only one line of code and should 
not use any kind of slicing or iteration.
"""

"""
Solution - Function that tests for substring
"""


def is_substring(example_string, test_string):
    """
    Function that returns True if test_string
    is a substring of example_string and False otherwise
    """
    return test_string in example_string
    

# Tests

example_string = "It's just a flesh wound."

print(is_substring(example_string, "just"))
print(is_substring(example_string, "flesh wound"))
print(is_substring(example_string, "piddog"))
print(is_substring(example_string, "it's"))
print(is_substring(example_string, "It's"))

# Output

#True
#True
#False
#False
#True