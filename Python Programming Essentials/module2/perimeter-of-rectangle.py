"""
Problem -
Write a Python function rectangle_perimeter that takes two parameters 
width and height corresponding to the lengths of the sides of a rectangle 
and returns the perimeter of the rectangle in inches.
"""

"""
Solution - Compute the length of a rectangle's perimeter, given its width and height.
"""

###################################################
# Rectangle perimeter formula
def rectangle_perimeter(width, height):
    """
    Returns the perimeter of a rectangle with the given width and height.
    """
    
    return width * 2 + height * 2


###################################################
# Tests

width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")


###################################################
# Expected output

#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.
