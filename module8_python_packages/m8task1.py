"""
implement a function "get_days_from _today(date)" that will return number of days from the current date
where <date> parameter has following format '2020-10-09'
notes: split <date> and convert it to int to use it in datetime
ignore hours and minutes - you need to get only days


"""

import datetime

def get_days_from_today(date:str)->int:

    date_list = [int(x) for x in text.split('-')]
    #p_date = date(date_list[0], date_list[1], date_list[2])
    #p_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    p_date = datetime.datetime(year=date_list[0], month=date_list[1], day=date_list[2]).date()
    now = datetime.date.today()
    return (now - p_date).days



    


text1 = "2020-10-09"
text = "2023-12-01"
now = datetime.date.today()

print(get_days_from_today(text))




