from datetime import datetime
from datetime import timedelta
from datetime import date

class Calendar:
    """
    Python: Monday = 0, Tuesday = 1, ... , Sunday = 6.
    ISO: Monday = 1, Tuesday = 2, ... , Sunday = 7.
    ISO week 1 is the week containing the first Thursday of the year. 
    Monday is the first day of the ISO week. 
    """
    
    months = {
        "standard": {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,
            "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}, 
        "leap": {"January": 31, "February": 29, "March": 31, "April": 30, "May": 31, "June": 30,
            "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}}
            
    def __init__(self):
        self.time_stamp = datetime.now()
        self.time_stamp_iso = self.time_stamp.isocalendar()

    def iso_equal(self):
        """
        Determines if the first partial week of the year and the first ISO week are the same week number. 
        """

        if date(self.time_stamp.year, 1, 1).weekday() in (0, 1, 2, 3, 6):
            return True
        return False

    def get_week(self):
        """
        Returns the current week number.
        Input: self
        Output: integer
        """

        if not self.iso_equal() and self.time_stamp.weekday() == 6:
            return self.time_stamp_iso[1] + 2
        if not self.iso_equal() or self.time_stamp.weekday() == 6:
            return self.time_stamp_iso[1] + 1 
        return self.time_stamp_iso[1]

    def reporting_week(self):
        """
        Prints the week number for reporting. 
        Input: Self
        Output: None
        """

        print("Week Numbers:")
        print(self.time_stamp)
        print(self.time_stamp_iso)
        print("Current = {}".format(self.get_week()))
        print("Reporting = {}".format(self.get_week() - 1))

    def leap_year(self):
        """
        Determines if the year is a leap year. 
        Input: self
        Output: boolean (Leap Year = True)

        if (year is not exactly divisible by 4) then (it is a common year)
        else if (year is not exactly divisible by 100) then (it is a leap year)
        else if (year is not exactly divisible by 400) then (it is a common year)
        else (it is a leap year)    
        """

        if self.time_stamp.year % 4 != 0:
            return False
        if self.time_stamp.year % 100 != 0:
            return True
        if self.time_stamp.year % 400 != 0:
            return False
        return True
    
def holiday(self):
    """
    Determines if the date is a holiday or not.
    Input: datetime.date
    Output: boolean (holiday = True) 
    """
    
    holidays = []  # array of holidays for the organization. 
    if self.time_stamp in holidays:
        return True
    return False  

def business_day(self):
    """
    Determines if the date is a business day or not.
    Input: datetime.date 
    Output: boolean (business day = True)
    """ 

    if self.time_stamp.weekday() not in (5, 6) and not holiday(self.time_stamp):
        return True 
    return False 
   
def n_business_days(self, n=-2):
    """
    Returns the date that is n business days from today.
    Use n < 0 to find past business days and n > 0 to find future business days. 
    Input: datetime.date, integer
    Output: date object for the date that is n business days from the input date.
    """

    business_days = 0
    calendar_days = 0 
    if n != 0:
        step = int(n/abs(n))
        while business_days != abs(n):
            calendar_days = calendar_days + step
            if business_day(self.time_stamp + timedelta(calendar_days)):
                business_days = business_days + 1
        return self.time_stamp + timedelta(calendar_days)
    return date


if __name__ == "__main__":
    c = Calendar()
    c.reporting_week()
