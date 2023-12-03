"""
implement a function that returns all sublist of a defind list
function should return at least one list with empty sublist [[]]

"""

def all_sub_lists(data):
    res = [[]]
    n = len(data)
    if n == 0:
        return [[]]
    
    for i in range(n):
        for j in range(i+1, n+1):
            numbers_copy1 = data[i:j:1]        
            res.append(numbers_copy1)
    return sorted(res, key = len)

    
    

numbers1 = [1, 2, 3, 4, 5, 6]
numbers2 = []
numbers3 = [1]
number4 = [1, 2]
print(all_sub_lists(numbers1))
print("_______________________")
print(all_sub_lists(numbers2))
print("_______________________")
print(all_sub_lists(numbers3))
print("_______________________")
print(all_sub_lists(number4))
