"""
Problem - 
Write a Python function is_leap_year that take as input the parameter year 
and returns True if year (an integer) is a leap year according to the Gregorian calendar 
and False otherwise. The Wikipedia entry for leap years contains a simple algorithmic rule for 
determining whether a year is a leap year. Your main task will be to translate this rule into Python.
"""

"""
Solution - Compute whether the given year is a leap year.
"""

###################################################
# Is leapyear formula
def is_leap_year(year):
    """
    Returns whether the given Gregorian year is a leap year.
    """	
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))


###################################################
# Tests

year = 2000
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1996
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1800
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 2013
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
###################################################
# Expected output

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
