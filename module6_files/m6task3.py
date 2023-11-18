"""
Read employees from a file and return list of employees
- read file with 'r' mode
- don't use with context manager
- return list of employees
- remove \n at the end of each employee (before returning the list)

example of input file:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19

example of output list:

['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
"""
def read_employees_from_file(path):
    res = []
    file = open(path, 'r')
    
    employees = file.readlines()
    for i in range(0,len(employees)):
        employees[i] = employees[i].rstrip("\n")
    file.close()
    return employees

#alternative to strip from the list:
# stripped = [s.strip() for s in list]

path = "./module6_files/task2txt/employees.txt"
print(read_employees_from_file(path))
