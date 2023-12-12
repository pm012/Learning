""""
Let's consider there is a string that contains integers (to simplify task).
The string defines parts of the profit. For example:
"The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
It's needed to implement a fucntion <generator_numbers> that will parse string and find all integers in the string. It
should work as generator that will return the numbers when requesting to it in a loop.


Function <generator_numbers(string="") should parse the string and return current number with the help of the yield.
Function <sum_profit(string)>  counts the sum of numbers received from <generator_numbers> and returns overal sum of profit 
stated in the string
"""
def generator_numbers(string=""):
    num_str = ""    
    for ch in string:
        if ch.isdigit():
            num_str+=ch
        else:
            if num_str.isdigit():
                yield int(num_str)
                num_str=""



def sum_profit(string):
    sum =0
    generator_numbers_iter = generator_numbers(string=string)
    for i in generator_numbers_iter:
        sum+=i
    return sum
    
    
        
    
text = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."

print(sum_profit(text))
