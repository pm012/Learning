"""
from the list of IP adresses IP = ['85.157.172.253',...,....]
Implement 2 follwing functions. 
First:
get_count_visists_from_ip using Counter returns dictionary where key is IP adress, value is number of IPs in the list
for example{'85.124.167.223': 2, ...}

Second get_frequent_visit_from_ip returns tuple with most frequently used IP in the list and number of it's occurences in 
the list
example: ('66.45.32.23', 4)


"""

from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)
    


def get_frequent_visit_from_ip(ips):
   return Counter(ips).most_common(1)[0]

ips_list = ['192.0.2.0', '192.0.2.1', '192.0.2.2',
'192.0.2.3', '192.0.2.4', '192.0.2.0',
'192.0.2.8', '192.0.2.8', '192.0.2.8',
'192.0.2.9', '192.0.2.10', '192.0.2.11',
'192.0.2.12', '192.0.2.13', '192.0.2.14',
'192.0.2.15']

print(get_count_visits_from_ip(ips_list))

print(get_frequent_visit_from_ip(ips_list))