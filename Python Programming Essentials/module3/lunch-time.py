"""
Problem - 
Write a Python function is_lunchtime that takes as input the parameters 
hour (an integer in the range [1,12]) and is_am (a Boolean “flag” that represents 
whether the hour is before noon). The function should return True when the input 
corresponds to 11am or 12pm (noon) and False otherwise. If the problem specification is unclear, 
look at the test cases in the provided template. Our solution does not use conditional statements.
"""

"""
Solution - Compute whether the given time is lunchtime.
"""

###################################################
# Is lunchtime formula
def is_lunchtime(hour, is_am):
    """
    Returns whether the given time, as represented by the hour
    and is_am, is lunchtime.
    """	
    return (hour == 11 and is_am) or (hour == 12 and not is_am)


###################################################
# Tests

def is_lunchtime_test(hour, is_am):
    """Tests the is_lunchtime function."""
    print(hour, end = "")
    if is_am:
        print("AM", end = "")
    else:
        print("PM", end = "")
    if is_lunchtime(hour, is_am):
        print(" is lunchtime.")
    else:
        print(" is not lunchtime.")

is_lunchtime_test(11, True)
is_lunchtime_test(12, True)
is_lunchtime_test(11, False)
is_lunchtime_test(12, False)
is_lunchtime_test(10, False)

###################################################
# Expected output

#11 AM is lunchtime.
#12 AM is not lunchtime.
#11 PM is not lunchtime.
#12 PM is lunchtime.
#10 PM is not lunchtime.
