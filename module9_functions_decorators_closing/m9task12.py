"""
with the help of reduce function calculate positive paymens amount and return its sum.
"""

from functools import reduce

def amount_payment(payment):
    return reduce((lambda x, y:  x+y), filter(lambda x: x>0, payment))


#with one lambda and conditional (using only reduce function)
def amount_payment1(payment):
    return reduce((lambda x, y: x + y if y > 0 else x), payment, 0)


all_payment = [1, -3, 4]

print(amount_payment(all_payment))