"""
Problem - 
Write a Python function future_value that takes three parameters 
present_value, annual_rate, and years and returns the future value of 
present_value dollars invested at annual_rate  percent interest, compounded annually for years. 
"""

"""
Solution - Compute the future value of a given present value, annual rate, and number of years.
"""

###################################################
# Future value formula
def future_value(present_value, annual_rate, years):
    """
    Returns the future value of the given money invested at an annual
    interest rate, compounded annually for the given number of years.
    """
    
    return present_value * (1 + 0.01 * annual_rate) ** years


###################################################
# Tests


present_value, annual_rate, years = 1000, 7, 10	
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")
    
present_value, annual_rate, years = 200, 4, 5
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")

present_value, annual_rate, years = 1000, 3, 20
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")


###################################################
# Expected output

#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.
