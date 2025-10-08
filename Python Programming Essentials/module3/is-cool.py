"""
Problem - 
Write a Python function is_cool that takes as input the string name and 
returns True if name is either "Joe", "John" or "Stephan" and returns False otherwise. 
(Let's see if Scott manages to catch this. ☺ )
"""

"""
Solution - Compute whether a person is cool.
"""

###################################################
# Is cool formula
def is_cool(name):
    """
    Returns whether the person with specified name is cool.
    """
    
    return (name == "Joe") or (name == "John") or (name == "Stephen")


###################################################
# Tests

name = "Joe"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

name = "John"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Stephen"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Scott"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

###################################################
# Expected output

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.
