"""
Problem -
Given p dollars, the future value of this money when compounded yearly 
at a rate of r percent interest for y years is p(1+0.01r)^y. 
(Remember that you don't need to understand how this formula works, 
only how to translate it into Python.) Write a Python statement that calculates 
and prints the value of 1000 dollars compounded at 7 percent interest for 10 years.
"""

"""
Solution - Compute the future value of a given present value, annual rate, and number of years.
"""

###################################################
# Future value formula
print(1000 * (1 + 0.01 * 7) ** 10)


###################################################
# Expected output
#1967.15135729