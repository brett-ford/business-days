import datetime as dt 

"""
if (year is not exactly divisible by 4) then (it is a common year)
else if (year is not exactly divisible by 100) then (it is a leap year)
else if (year is not exactly divisible by 400) then (it is a common year)
else (it is a leap year)
"""

def leap_year(date):
    # Determines if the input year is a leap year. 
    # Input: date object
    # Output: boolean (Leap Year = True)
    
    if date.year % 4 != 0:
        return False
    if date.year % 100 != 0:
        return True
    if date.year % 400 != 0:
        return False
    return True

