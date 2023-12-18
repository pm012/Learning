"""
rewrite following using UserList (count sum for only positive values):
payment = [1, -3, 4]


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum

Create AmountPaymentList class inhert it from UserList. Create function amount_payment within the  created class
"""
from collections import UserList
from functools import reduce


class AmountPaymentList(UserList):
    def amount_payment(self):
        return reduce(lambda x, y: x + y if y > 0 else x, self.data, 0)
    

my_list = AmountPaymentList([1, -3, 7])

print(my_list.amount_payment())
        
        
            
                
        