def make_request(keys, values):
    if len(set(keys)) != len(values):
        print("Error: Unique keys are not equal to values")
        return dict()
    else:
        return dict(map(lambda i, j : (i,j), keys, values))
    

keys_list = ["name", "email", "age", "site"]
values_list = ["John Doe", "john.doe@gmail.com", "12", "https://john_doe.com.ua"]
#print(make_request(keys_list, values_list))
from random import random, seed

seed(1)

for i in range(5):
    print(random())



