"""
Problem -
Write a Python function miles_to_feetstart that takes a parameter miles 
and returns the number of feet in miles. 
"""

"""
Solution - Compute the number of feet corresponding to a number of miles.
"""

###################################################
# Miles to feet conversion formula
def miles_to_feet(miles):
    """
    Returns the number of feet in the given number of miles.
    """
    
    return miles * 5280


###################################################
# Tests

miles = 13
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")
    
miles = 57
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

miles = 82.67
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")


###################################################
# Expected output

#13 miles equals 68640 feet.
#57 miles equals 300960 feet.
#82.67 miles equals 436497.6 feet.