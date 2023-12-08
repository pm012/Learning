"""
create function decimal_average(number_list, signs_count) that will calculate average of Decimal type
with precision of digits <signs_count>. Parameter number_list - list of numbers

examples: 
decimal_average([3, 5, 77, 23, 0.57], 6) -> 21.714
decimal_average([31, 55, 177, 2300, 1.57], 9) -> 512.91400
"""

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec=signs_count
    list_decimals = [Decimal(x) for x in number_list]
    try: 
        return sum(list_decimals)/Decimal(len(list_decimals))
    except ZeroDivisionError:
        return list()


print(decimal_average([3, 5, 77, 23, 0.57], 6)) #-> 21.714
print(decimal_average([31, 55, 177, 2300, 1.57], 9)) #-> 512.91400