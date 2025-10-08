"""
Problem - 
Write a Python function name_lookup that takes a string first_name that corresponds to one of (
"Joe", "Scott", "John" or "Stephen") and then returns their corresponding last name ("Warren", "Rixner",
"Greiner" or "Wong"). If first_name doesn't match any of those strings, 
return the string "Error: Not an instructor".
"""

"""
Solution - Compute instructor's last name, given the first name.
"""

###################################################
# Name lookup formula
def name_lookup(first_name):
    """Returns the instructor's last name."""
    
    if first_name == "Joe":
        return "Warren"
    elif first_name == "Scott":
        return "Rixner"
    elif first_name == "John":
        return "Greiner"
    elif first_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"


###################################################
# Tests
    
first_name = "Joe"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "Scott"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "John"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "Stephen"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "Mary"
print(first_name + "'s last name is", name_lookup(first_name))
      

###################################################
# Expected output

#Joe's last name is Warren
#Scott's last name is Rixner
#John's last name is Greiner
#Stephen's last name is Wong
#Mary's last name is Error: Not an instructor
