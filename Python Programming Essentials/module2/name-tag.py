"""
Problem - 
Write a Python function name_tag that takes as input the parameters 
first_name and last_name (strings) and returns a  string of the form "My name is % %." 
where the percents are the strings first_name and last_name. Reference the test cases 
in the provided template for an exact description of the format of the returned string.
"""

"""
Solution - Compute a name tag, given the first and last name.
"""

###################################################
# Name tag formula
def name_tag(first_name, last_name):
    """
    Returns a name tag string with the given name.
    """
    
    return "My name is " + first_name + " " + last_name + "."

    
###################################################
# Tests
    
first_name, last_name = "Joe", "Warren"
print(name_tag(first_name, last_name))

first_name, last_name = "Scott", "Rixner"
print(name_tag(first_name, last_name))

first_name, last_name = "John", "Greiner"
print(name_tag(first_name, last_name))


###################################################
# Expected output

#My name is Joe Warren.
#My name is Scott Rixner.
#My name is John Greiner.
