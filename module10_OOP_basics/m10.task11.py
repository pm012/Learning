"""
count the number of digits in string in NumberString as child of UserString class.
Use method number_count(self)

"""
from collections import UserString
from functools import reduce

# case1: using loop
# class NumberString(UserString):
#     def number_count(self):
#         cnt = 0
#         for ch in self.data:
#             if ch.isdigit():
#                 cnt+=1
#         return cnt
    
#case2: using reduce
class NumberString(UserString):
     def number_count(self):
         
         return reduce(lambda x, y: x+1 if y.isdigit() else x, self.data, 0)

my_str = NumberString("The third congress of the UFA was held in Kyyiv in 1991. It was sold 34 aircrafts for spaceshop shattles for 3400000000B$")
print(my_str.number_count())
            