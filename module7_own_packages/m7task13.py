"""
Function <get_employees_by_profession(path, profession)>  find in a file on a given <path>
all employees with a specified <profession>.
Requirements:
1. Open file using with context meneger for reading.
2. Read file records using readlines()
3. Using <find> method find all recrods in a file where searched profession is present
4. Join all found records using <join> method (remove \n and trailins spases)
5. replace <profession> with "" using replace method
6. Return the resultin string
"""
import re

def get_employees_by_profession(path, profession):
    lst=[]
    
    with open(path, 'r') as file:
        lst = file.readlines()
    lst = [record for record in lst if record.find(profession)!=-1]
    print(lst)
    res = "".join(lst).rstrip().replace("\n","")    
    res = re.sub(r"\s+"," ",res)
    return res.replace(profession, "").rstrip()
    
path = "./module7_own_packages/professions.txt"
print(get_employees_by_profession(path, "cook"))

        
        

    

    
        
    
    
        
            
    
    
