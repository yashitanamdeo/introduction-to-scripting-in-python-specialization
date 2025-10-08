"""
Problem - 
Given a string example_string with at least three characters, write a Python expression using two 
string slices that produces the string formed by selecting the first three characters and 
the last three characters in example_string.
"""

"""
Solution - Another example of slice selection for lists
"""

# Create a string formed by selecting the first three characters of example_string
# plus the last three characters of example_string
example_string = "It's just a flesh wound"
print(example_string)

# Note that the default values for a slice are the start and end of the string
solution_string = example_string[: 3] + example_string[-3 :]
print(solution_string)

# Output should be 
#It's just a flesh wound
#It'und