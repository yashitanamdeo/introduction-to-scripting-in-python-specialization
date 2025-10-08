"""
Problem - 
Challenge: Write a Python function print_digits that takes an integer number 
in the range [0, 100), (i.e., at least 0, but less than 100) and prints the message 
"The tens digit is %, and the ones digit is %.", where the percent signs should be replaced 
with the appropriate values. (Hint: Use the arithmetic operators for integer division // and 
remainder % to find the two digits. Note: that this function should 
print the desired message, rather than returning it as a string.) 
"""

"""
Solution - Compute and print tens and ones digit of an integer in [0,100).
"""

###################################################
# Digits function
def print_digits(number):
    """
    Prints the tens and ones digit of an integer in [0,100).
    """
    
    print("The tens digit is " + str(number // 10) + ", and the ones digit is " + 
          str(number % 10) + ".")

    
###################################################
# Tests
    
print_digits(42)
print_digits(99)
print_digits(5)


###################################################
# Expected output

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
