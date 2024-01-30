import json

d = {"a": 1}
l = [1, 2.2]
t = (3, 4)
s = "I am string!"

with open('store.json', 'w') as file:
    json.dump(d, file)

with open('store.json', 'r') as file:
    d_copy = json.load(file)


print (d is d_copy)
print(d, d_copy)