"""
Problem -
Write a Python function name_and_age that takes as input the parameters 
name(a string) and age(a number) and returns a string of the form "% is % years old." 
where the percents are the string forms of name and age. 
Reference the test cases in the provided template for an exact description of the 
format of the returned string. 
"""

"""
Solution - Compute the statement about a person's name and age, given the person's name and age.
"""

###################################################
# Name and age formula
def name_and_age(name, age):
    """
    Returns a string stating the person's age.
    """
    
    return name + " is " + str(age) + " years old."


###################################################
# Tests
    
name, age = "Joe Warren", 56
print(name_and_age(name, age))

name, age = "Scott Rixner", 40
print(name_and_age(name, age))

name, age = "John Greiner", 46
print(name_and_age(name, age))


###################################################
# Expected output

#Joe Warren is 56 years old.
#Scott Rixner is 40 years old.
#John Greiner is 46 years old.
