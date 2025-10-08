"""
Problem - 
Write a Python function circle_area that takes a single parameter radius corresponding 
to the radius of a circle in inches and returns the the area of a circle with 
radius in square inches. Do not use π=3.14, instead use the math module to supply 
a higher-precision approximation to π.
"""

"""
Solution - Compute the area of a circle, given the length of its radius.
"""

# Import the math module to access the exact value of pi
import math
PI = math.pi

###################################################
# Circle area formula

def circle_area(radius):
    """
    Returns the area of a circle of the given radius.
    """
    return PI * radius ** 2


###################################################
# Tests

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")


###################################################
# Expected output

#A circle with a radius of 8 inches has an area of 201.06192983 square inches.
#A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
#A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.
