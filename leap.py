#Determines if a year is a leap year. Leap year = true, common year = False.
#if (year is not exactly divisible by 4) then (it is a common year)
#else if (year is not exactly divisible by 100) then (it is a leap year)
#else if (year is not exactly divisible by 400) then (it is a common year)
#else (it is a leap year)
def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

year = int(input("What year would you like to test?"))

if leap_year(year) == True:
    print(year, """is a leap year!""")
elif leap_year(year) == False:
    print ("""Sorry,""", year, """is not a leap year""")