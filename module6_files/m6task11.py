"""Read the file from the 10-th task and
create a list of <username:password> from each record
- Use with in 'rb' mode to read file. 
"""

def get_credentials_users(path):
    res = []
    with open(path, 'rb') as file:
        for record in file:
            res.append(record.decode().rstrip("\n"))

    return res


path = path = "./module6_files/task10txt/passwords.bin"
print(get_credentials_users(path))
        
