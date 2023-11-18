"""
write_employes_to_file(employee_list, path):
- receives 2 parameters <path> - path to the file and <employee_list> - list of lists of employees as you can see in the example below
[['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

- write all information to the file using 'w' mode
- don't use context manager <with>
- write employees,  so that each employee is placed on new line

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
"""

def write_employees_to_file(employee_list, path):
    file = open(path, 'w')
    str = ""
    for list_outer in employee_list:
        for list_iner in list_outer:
           str +=  list_iner+"\n"
    file.write(str)
    file.close()

lst = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
path = "./module6_files/task2txt/employees.txt"
write_employees_to_file(lst, path)