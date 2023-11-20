"""
function <def save_credentials_users(path, users_info)> saves information 
about users  with passwords to the binary file.
Where:
- <path >  - filepath
- users_info - is a dictionary {'andry' : 'uyro18890D', steve':'ooppjM13LL9e'}, where login - key and value is password

Requirements:
- each record should have username:password (such format is used in Basic Authentication)
- Open file and save key and value from the dictionary users_info in format <username:password> for each element of the 
users_info dictionary
"""

def save_credentials_users(path, users_info):    

        with open(path, 'wb') as file:
                for key, value in users_info.items():
                    file.write(bytes(f"{key}:{value}\n" ,'utf-8'))


path = "./module6_files/task10txt/passwords.bin"
users = {'andry' : 'uyro18890D', 'steve':'ooppjM13LL9e'}
save_credentials_users(path, users)
                
                
            