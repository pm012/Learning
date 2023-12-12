"""
There are names of users in list 
name = ["dan", "jane", "steve", "mike"]
Create a function normal_nmae that takes the name list as a parameter and returns the list of name with the capitalized first 
letter.
Requirements:
use function map. Don't forget to apply type conversion for map

"""
def normal_name(list_name):
    normal_names = list()
    for i in map(lambda x: x.capitalize(), list_name):
        normal_names.append(i)
    return normal_names



name = ["dan", "jane", "steve", "mike"]
print(normal_name(name))
