"""Thre is a text file that has monthly salary for each emploee
of the company:
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

total_salary(path) should take filename as  a <path> parameter and return float number for total amount of salaries
- returns float
- uses only readline method to read file
- don't use context manager "with"
"""

def total_salary(path):    
    file = open(path)
    try:

        line = "abc"
        res = 0.0
        while bool(line):
            line = file.readline()
            if  line:
                 res += float(int(line.split(",")[1]))

    except Exception as e:
         print(e)
    finally:
        if  not file.closed and file.readable():
                file.close()
         
    return res

path = "./module6_files/task1txt/total_salary.txt"
print(total_salary(path))


        
