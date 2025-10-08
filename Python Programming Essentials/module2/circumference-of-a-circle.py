"""
Problem - 
Write a Python function circle_circumference that takes a single parameter radius 
corresponding to the radius of a circle in inches and returns the the circumference 
of a circle with radius in inches. Do not use π=3.14, instead use the math module 
to supply a higher-precision approximation to π.
""" 

"""
Solution - Compute the circumference of a circle, given the length of its radius.
"""

import math
PI = math.pi

###################################################
# Circle circumference formula

def circle_circumference(radius):
    """
    Returns the circumference of a circle of the given radius.
    """
    
    return 2 * PI * radius


###################################################
# Tests

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")


###################################################
# Expected output

#A circle with a radius of 8 inches has a circumference of 50.2654824574 inches.
#A circle with a radius of 3 inches has a circumference of 18.8495559215 inches.
#A circle with a radius of 12.9 inches has a circumference of 81.0530904626 inches.
