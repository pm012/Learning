"""
count how many days in a motns. function <get_days_in_month> takes 2 parameters month from 1 to 12 and 
datetime 4 digit string  '1894' or 4 digit integer 1893. Function should correctly return number of days in a month 
test additionaly on February (2) of the leap and regular year

"""


from datetime import date, datetime

def get_days_in_month(month, year):
    int_year=0
    if type(year).__name__=='int' and type(month).__name__=='int' and month in range(1, 13):
        int_year=year
    elif type(year).__name__=='str' and len(year)==4 and year.isdigit() and type(month).__name__=='int': 
        int_year=int(year)
    else:
        print("Incorrect data. Month should be int [from 1 to 12], year should be 4 digits(string or integer)")
        return None
    next_month, next_year = (month+1, year) if month<12 else (1, year+1)
    next_month_date = datetime(year=next_year, month=next_month, day=1).date()
    this_month_date = datetime(year=int_year, month=month, day=1).date()
    
    return (next_month_date - this_month_date).days


print(get_days_in_month(12, 2024))
    

    



    

