"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        raise ValueError("Year is out of range")
    
    # Get the first day of the current month
    first_day = datetime.date(year, month, 1)
    
    # Get the first day of the next month
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    
    # Subtract to get the difference in days (i.e., number of days in the current month)
    delta = next_month - first_day
    return delta.days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        return False
    if month < 1 or month > 12:
        return False
    days_in_this_month = days_in_month(year, month)
    return 1 <= day <= days_in_this_month

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    min_year = datetime.MINYEAR
    max_year = datetime.MAXYEAR
    
    if year1 < min_year or year1 > max_year or year2 < min_year or year2 > max_year:
        return 0

    if not is_valid_date(year1, month1, day1) or not is_valid_date(year2, month2, day2):
        return 0

    # Use datetime.date to create date objects
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    if date2 < date1:
        return 0

    return (date2 - date1).days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        return 0

    # Use datetime.date to get today's date
    today = datetime.date.today()

    if not is_valid_date(year, month, day):
        return 0

    birth_date = datetime.date(year, month, day)

    if birth_date > today:
        return 0

    return days_between(year, month, day, today.year, today.month, today.day)
