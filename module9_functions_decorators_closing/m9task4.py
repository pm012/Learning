"""
Create a function discount_price(discount) that should define and return inner function
for calculating real price with discount

The call of the function will return a function that will calculate goods price with the discount that equals <discount>

For example:
cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))

should  retun 
85.0
90.0
95.0

"""


def discount_price(discount):
    def calculate_discount(price):
        return price*(1-discount)
    
    return calculate_discount



cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)


price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))
