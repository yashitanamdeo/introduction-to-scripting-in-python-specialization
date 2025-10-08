"""
Problem - 
Challenge: Given numbers a, b, and c, the quadratic equation ax^2+bx+c=0 can have zero, 
one or two real solutions (i.e; values for x that satisfy the equation). The quadratic formula can be used
to compute these solutions: x = (-b ± √(b^2 - 4ac)) / 2a. The expression b^2 - 4ac 
is the discriminant associated with the equation. If the discriminant is positive, the equation has two solutions. 
If the discriminant is zero, the equation has one solution. Finally, if the discriminant is negative, 
the equation has no solutions. Write a Python function smaller_root that takes an input the numbers 
a, b, and c and returns the smaller solution to this equation if one exists. If the equation has no 
real solution, print the message "Error: No real solutions" and simply return. Note that, in this case, 
the function will actually return the special Python value None.
"""

"""
Solution - Compute the smaller root of a quadratic equation.
"""

###################################################
# Smaller quadratic root formula
def smaller_root(coeff_a, coeff_b, coeff_c):
    """
    Returns the smaller root of a quadratic equation with the
    given coefficients.
    """
    
    discriminant = coeff_b ** 2 - 4 * coeff_a * coeff_c
    if discriminant < 0 or coeff_a == 0:
        print("Error: No real solutions")
    else:
        discriminant_sqrt = discriminant ** 0.5
        # Choose the positive or negative square root that leads to a smaller root.
        if coeff_a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-coeff_b + smaller) / (2 * coeff_a)


###################################################
# Tests

coeff_a, coeff_b, coeff_c = 1, 2, 3
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 2, 0, -10
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


coeff_a, coeff_b, coeff_c = 6, -3, 5
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


###################################################
# Expected output

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None
