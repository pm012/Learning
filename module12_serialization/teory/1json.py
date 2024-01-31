import json

d = {"a": 1}
d2 = {2: 1}
l = [1, 2.2]
t = (3, 4)
s = "I am string!"

print(json.dumps(d))
print(json.dumps(d2))
print(json.dumps(l))
print(test:=json.dumps(t))
print(json.dumps(s))
print(json.loads(test))
l = [11, 12]
print(json.loads(l))

with open('./module12_serialization/teory/store.json', 'w') as file:
    json.dump(d, file)

with open('./module12_serialization/teory/store.json', 'r') as file:
    d_copy = json.load(file)


print (d is d_copy)
print(d, d_copy)