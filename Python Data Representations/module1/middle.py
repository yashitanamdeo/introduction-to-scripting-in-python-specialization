"""
Problem -
Given a string example_string with at least two characters, write a Python expression using a 
string slice that selects all but the first and last characters in example_string.
"""

"""
Solution - Slice selection for lists
"""

# Create a string formed by selecting all but the first and last letters of example_string
example_string = "It's just a flesh wound"
print(example_string)

# Note that negative indices select characters from the end of the string
solution_string = example_string[1 : -1]
print(solution_string)

# Output should be 
#It's just a flesh wound
#t's just a flesh woun