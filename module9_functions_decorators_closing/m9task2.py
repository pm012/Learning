"""
Implement function  get_discount_price_customer.
It should get 2 parameters:
price - the product price
customer - dictionary with the data of ccustomer in following format:
{"name":"Dima"} or {"name":"Boris","discount":0.15}

Use DEFAULT_DISCOUNT field to define the discount for customer that has no discount in the dictionary

"""


DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if 'discount' in customer.keys():
        return price *(1 - customer['discount'])
    else:
        return price *(1-DEFAULT_DISCOUNT)
    


d1 = {"name":"Dima"} 
d2 = {"name":"Boris","discount":0.15}
print(get_discount_price_customer(100, d1))
print(get_discount_price_customer(100, d2))
