"""
function <get_str_date> should convert date in ISO format (2021-05-27 17:08:34.149Z) 
to date and return it in the following format (Thursday 27 May 2021)

"""

from datetime import datetime

def get_str_date(date):
    lst = [int(x.strip()) for x in (date[0:11].split('-')) if x.strip().isdigit()]
    return str(datetime(year=lst[0], month=lst[1], day=lst[2]).date().strftime('%A %d %B %Y'))




iso_date = '2021-05-27 17:08:34.149Z'
print(get_str_date(iso_date))
#print(iso_date[0:11].split('-').strip())
