"""
implement 
def add_employee_to_file(record, path) that adds employee record <record> to the file <path>
Each employee should be added as new line
Open file in ammendment mode 'a' 
Do not use context manager <with>

"""

def add_employee_to_file(record, path):
    file = open(path, 'a')
    file.write(record+"\n")
    file.close()






    
path = "./module6_files/task4txt/employees.txt"   
list = ["record1", "record2", "record3"]
for record in list:
    add_employee_to_file(record, path)
    
