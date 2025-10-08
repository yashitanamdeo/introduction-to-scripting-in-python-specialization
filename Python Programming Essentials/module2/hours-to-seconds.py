"""
Problem - 
Write a Python function total_seconds that takes three parameters 
hours, minutes, and seconds and returns the total number of 
seconds for hours, minutes, and seconds.
"""

"""
Solution - Compute the number of seconds in a given number of hours, minutes, and seconds.
"""

###################################################
# Hours, minutes, and seconds to seconds conversion formula
def total_seconds(hours, minutes, seconds):
    """
    Returns the number of seconds in the given number of hours, minutes, and seconds.
    """
    
    return (hours * 60 + minutes) * 60 + seconds


###################################################
# Tests

hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

###################################################
# Expected output

#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.