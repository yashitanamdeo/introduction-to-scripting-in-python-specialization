"""
Problem - 
Given a non-empty string example_string, write a Python expression that produces the two-character 
string formed by selecting the first and last characters of example_string.
"""

"""
Solution - Item selection for lists
"""

# Create a string formed by selecting the first and last letters of example_string
example_string = "It's just a flesh wound"
print(example_string)

# Note that negative indices select characters from the end of the string
solution_string = example_string[0] + example_string[-1]
print(solution_string)

# Output should be 
#It's just a flesh wound
#Id