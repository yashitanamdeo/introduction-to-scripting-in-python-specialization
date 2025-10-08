"""
Problem - 
Write a Python function rectangle_area that takes two parameters width and height 
corresponding to the lengths of the sides of a rectangle and returns 
the area of the rectangle in square inches. 
"""

"""
Solution - Compute the area of a rectangle, given its width and height.
"""

###################################################
# Rectangle area formula
def rectangle_area(width, height):
    """
    Returns the area of a rectangle with the given width and height.
    """
    
    return width * height


###################################################
# Tests

width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
    
width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

    
###################################################
# Expected output

#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.
