import datetime as dt

"""
Find the date that is n business days from today. 
Use n < 0 to find past business days and n > 0 to find future business days. 
"""


def holiday(date):
    """Determines if the date is a holiday or not."""
    # input: date object
    # output: boolean (holiday = True) 
    
    holidays = []  # array of holidays for the organization. 
    if date in holidays:
        return True
    return False  


def business_day(date):
    """Determines if the date is a business day or not.""" 
    # input: date object
    # output: boolean (business day = True)
    # Sunday = 0, Monday = 1, ... , Saturday = 6
 
    day_of_week = (int(date.weekday()) + 1) % 7
    if day_of_week not in [0, 6] and not holiday(date):
        return True 
    return False 
   

def n_business_days(date, n=-2):
    """Returns the date that is n business days from today."""
    # input: date object for today's date
    # input: integer representing the number of business days before or after the date.
    # output: date object for the date that is n business days from the input date.
       
    business_days = 0
    calendar_days = 0 

    if n != 0:
        step = int(n/abs(n))
        while business_days != abs(n):
            calendar_days = calendar_days + step
            if business_day(date + dt.timedelta(calendar_days)):
                business_days = business_days + 1
        return date + dt.timedelta(calendar_days)
    return date


def main():
    today = dt.date.today()
    print(today)
    n = int(input('Number of business days?:'))
    print(n_business_days(today, n))
    print()
    

if __name__ == '__main__':
    main()
