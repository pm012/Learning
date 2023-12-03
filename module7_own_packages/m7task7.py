"""

<list_data> is list of list with integers.
if the list length is more than 2 elements function should remove
minimum and maximum values from each list
after deleting minimum and maximum values all lists should
be joined ton the resulting list, sorted in desc order and return it as a result
for example [[1,2,3],[3,4], [5,6]]
should be returned as [6, 5, 4, 3, 2]
"""

def data_preparation(list_data):
    res = list()
    
    for number_list in list_data:        
        if len(number_list) > 2:
            min_value, max_value = min(number_list), max(number_list)
            number_list = [num for num in number_list if num != min_value and num != max_value]
        res.extend(number_list)

    return sorted(res, reverse=True)


data = [[1,2,3],[3,4], [5,6]]
print(data_preparation(data))
            
        
    
    
        
            
            
            
                
                
            
    
    