"""
Problem - 
Write a Python function is_even that takes as input the parameter number 
(an integer) and returns True if number is even and False if number is odd. 
Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.
"""

"""
Solution - Compute whether an integer is even.
"""

###################################################
# Is even formula
def is_even(number):
    """
    Returns whether number is even.
    """
    return (number % 2) == 0


###################################################
# Tests

number = 8
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")
    
number = 3
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")
    
number = 12
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")

###################################################
# Expected output

#8 is even.
#3 is odd.
#12 is even.
