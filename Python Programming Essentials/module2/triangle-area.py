"""
Problem - 
Challenge: Write a Python function triangle_area that takes the parameters 
x_0, y_0, x_1, y_1, x_2, and y_2 (all numbers), and returns the area of the triangle 
with vertices (xo,y0), (x1,y1), and (x2,y2).
(Hint: use the function point_distance as a helper function and apply Heron's formula.)
"""

"""
Solution - Compute the area of a triangle (using Heron's formula),
    given its side lengths.
"""

###################################################
# Triangle area (Heron's) formula
# Hint:  Use point_distance as a helper function.

def point_distance(x_0, y_0, x_1, y_1):
    """
    Returns the Euclidian distance between two points (x0,y0) and (x1,y1).
    """
    
    return ((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5
    
def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    """
    Returns the area of a triangle with vertices (x0,y0), (x1,y1), and (x2,y2).
    """
    
    # Compute the lengths of the three sides.
    len_01 = point_distance(x_0, y_0, x_1, y_1)
    len_02 = point_distance(x_0, y_0, x_2, y_2)
    len_12 = point_distance(x_1, y_1, x_2, y_2)
    
    # Compute the semi-perimeter length, i.e., half of the perimeter length.
    semi_perim = (len_01 + len_02 + len_12) / 2
    
    # Compute the area according to Heron's formula.
    return (semi_perim * (semi_perim - len_01) * (semi_perim - len_02) * (semi_perim - len_12)) ** 0.5


###################################################
# Tests

def test(x_0, y_0, x_1, y_1, x_2, y_2):
    """Tests the triangle_area function."""
    
    print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + "),")
    print("(" + str(x_1) + "," + str(y_1) + "), and")
    print("(" + str(x_2) + "," + str(y_2) + ") has an area of")
    print(str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 0, 0, 3, 4, 1, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = -2, 4, 1, 6, 2, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 10, 0, 0, 0, 0, 10
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")


###################################################
# Expected output

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
