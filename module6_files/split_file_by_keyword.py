import sys
import time
import random
#sys.argv list of parameters
file = None
txt_list = None
files_count = 0
path = None

#Open file to parse
def open_file(path_param = './module6_files/mytxt/', filename = 'Orwel1984.txt', split_by=r"*Chapter \d{1,}"):
    global path
    path = path_param
    full_path = path + filename        
    global txt_list
    try:
        file = open(full_path)
        txt_list = file.readlines()
    except FileNotFoundError:        
        print(f"File not found {full_path}")
    finally:
        file.close()
        print("File closed") 


#generate file format
def generate_fname():
    global files_count
    timestamp = time.strftime("%YYYY%MM$dd%H%M%S")
    files_count += 1
    return f"file_{files_count}_{timestamp}.txt"

#write splited file to separate files
def create_files():
    global path
    for item in txt_list:
        try:
            f = open(path+"res/"+generate_fname(), 'a')
            if item.find("Chapter ") ==-1:
                f.write(item)
            else:
               f.close()
               break

        except FileNotFoundError:
            print("Error writing file check your dir")
        finally:
            f.close()
            

# main flow method        
def flow():
    if len(sys.argv) == 4:
        global path
        global file 
        path = sys.argv[0]
        open_file(path, sys.argv[1], sys.argv[2])
        create_files()
    elif len(sys.argv)==1:
        print("Default parameters are used:")
        print("'/Documents/test.txt' , 'file_name.txt", r"^Chapter \d{1,}")
        open_file()
        create_files()        
    else:
        print("Set valid command line parameters 'path', 'filename', 'split_by_regex' e.g.: '/Documents/test.txt' , 'file_name.txt", r"^Part \d{1,}")
        print(" Or leave command line parameters empty for the default: './module6_files/mytxt' , 'Orwel1984.txt', '^Chapter \d{1,}' are set by default" )
        return 
    


flow()
    
    
        









    