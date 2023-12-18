"""
Create class IDException, which inherits class Exception.
Implement add_id(id_list, employee_id) function, that adds to id_list user's id <employee_id> and returns 
updated id_list.
Function add_id will call own exception IDException, if employee_id doesn't start with '01',
otherwise employee_id should be added to id_list

"""
class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    result = id_list
    if employee_id[:2] != '01':
        raise IDException
    else:
        result.append(employee_id)
    return result


ids_list = ["928374298-True", '023984239-True', "0183493847-False", "02932038-True"]
id_db = ["1928379-base"]


for id in ids_list:
    try:
        id_db=add_id(id_db, id)
    except IDException:
        print("Exception is caught")

print(id_db)


    
        
    
        
    
