"""
Problem - 
Challenge:
Powerball is lottery game in which 6 numbers are drawn at random. 
Players can purchase a lottery ticket with a specific number combination and, 
if the number on the ticket matches the numbers generated in a random drawing, 
the player wins a massive jackpot. Write a Python function powerball that takes no arguments 
and prints the message "Today's numbers are %, %, %, %, and %. The Powerball number is %.".
The first five numbers should be random integers in the range [1,60), i.e., 
at least 1, but less than 60. In reality, these five numbers must all be distinct, 
but for this problem, we will allow duplicates. The Powerball number is a random integer in the range
[1,36), i.e., at least 1 but less than 36. Note that this function should print the
desired message, rather than returning it as a string.
"""

"""
Solution - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function

def powerball():
    """
    Prints Powerball lottery numbers.
    """
    
    # Note that including the optional argument end = "" to print() cause
    # print to NOT generate a newline
    
    print("Today's numbers are " + str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "") 
    print(str(random.randrange(1, 60)) + ", and ", end = "")
    print(str(random.randrange(1, 60)) + ". The Powerball number is ",  end = "") 
    print(str(random.randrange(1, 36)) + ".")

    
###################################################
# Tests
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.
