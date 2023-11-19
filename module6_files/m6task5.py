"""
There is a file with a following structure:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Where first part of the first record is the key of MongoDB database. It consists of 12 bytes or 24 symbols.
The second part is the cat's nickname and its age.
All parts of the record is devided by ','

Implement a function get_cats_info(path) that will return list of dictionaries with cats data in following format:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]

<path> is the filepath 

Requirements:
- read the file contents using 'r' mode
- Use context manager 'with'
- return list of cats in the required format


"""


def get_cats_info(path):
    res = []
    
    with open(path, 'r') as file:
                
        for record in file:
            cat_info = record.split(',')
            res.append({"id" : cat_info[0], "name" : cat_info[1], "age": cat_info[2].rstrip("\n")})

    return res

path = "./module6_files/task5txt/cats.txt"

print(get_cats_info(path))
        


