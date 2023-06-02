
def is_leap(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


def days_in_month(year, month):
    """ This code takes an input in the form of year and month from users and return the number of days in the said month """

    is_leap_year = is_leap(year)

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap_year and month == 2:
        return "February in a leap year has 29 days."
    days = month_days[month - 1]
    return f"This month has {days} days."
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month (e.g 1 for January, 2 for February, etc): "))
days = days_in_month(year, month)
print(days)







