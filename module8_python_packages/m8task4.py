""""
get_numbers_ticket(min, max, quantity) should return
quantity number of digits  from min to max range 
min should be >=1 and max should be <=1000 if quantity is not in range or min/max does't match the requirements 
should be returned empty list
list with values should be sorted asc

"""

from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min>=1 and max<=1000 and quantity in range(min, max+1):
        result = set()
        while len(result)<quantity:
            result.add(randrange(min, max))
        return sorted(list(result))
    else: 
        return list()
    

print(get_numbers_ticket(1, 49,4))

