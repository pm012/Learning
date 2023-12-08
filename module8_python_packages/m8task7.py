"""
There is a named tuple that contains cats in a variable Cat: 1-st place is nickname, 2-nd - age, 3-rd owner
If conver_list function takes as a parameter cats list of name duples:
[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
function should return list of dictionaries:
[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]

if cats gets list of dictionaries as a parameter it should return named tuple as a result

"""

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def convert_list(cats):
    result = list()
    if isinstance(cats[0], dict):                
        for cat in cats:
            result.append(Cat(cat["nickname"],cat['age'],cat['owner']))
        return result
    elif isinstance(cats[0], Cat):        
        for cat in cats:
            result.append({"nickname":cat.nickname, "age":cat.age, "owner":cat.owner})
        return result
        
    else:
        return None

dl = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
tl=[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
print(convert_list(tl))
#print(type(Cat("Mick", 5, "Sara")).__name__)
d = {"nickname": "Mick", "age": 5, "owner": "Sara"}
#print(d["nickname"])