"""
given list with following structure: [1, 2, [3, 4, [5, 6]], 7] 
using recursion convert it to the flat list: [1,2,3,4,5,6,7]
Requirements:
1 if input list is empty return empty list
2 if the first element of the list is list 
    - get first list recurcively calling function with the first element of the list
    - get another list, recursively cllaing function with the rest of list without the first element
    - return concatenation of 2 lists
3 If the first element of the list is not a list:
    - get the first list containing the first element of the list
    - get another list, calling recursively function with the rest of the list without the first element
    - return concatenation of the lists

"""


def flatten(data):
    if len(data)==0:
        return list()
    
    if type(data[0]).__name__ =='list':        
         return flatten(data[0]) + flatten(data[1:])
    else:
        return [data[0]]+flatten(data[1:]) 
    
tst_lst =  [1, 2, [3, 4, [5, 6]], 7] 
result= flatten(tst_lst)
print(result)
