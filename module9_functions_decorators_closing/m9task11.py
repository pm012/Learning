"""
Calculate the sum of numbers = [3, 4, 6, 9, 34, 12] with the help of redce function.

sum_numbers(numbers)

"""

from functools import reduce

def sum_numbers(numbers):
    return reduce((lambda x, y: x+y), numbers)


nums = [3, 4, 6, 9, 34, 12]
print(sum_numbers(nums))