import sys
import time
import random
import re
#sys.argv list of parameters
file = None
lines = None
files_count = 0
path = None

#Open file to parse
def open_file(path_param = './module6_files/mytxt/', filename = 'Orwel1984.txt'):
    global path
    path = path_param
    full_path = path + filename        
    global lines
    try:
        file = open(full_path, 'r')
        lines = file.readlines()
        
    except FileNotFoundError:        
        print(f"File not found {full_path}")
    finally:
        file.close()
        print("File closed") 


#generate file format
def generate_fname():
    global files_count
    timestamp = time.strftime("%Y%m$d%H%M%S")
    files_count += 1
    return f"file_{files_count}_{timestamp}.txt"

#write splited file to separate files
def create_files(text_markup = r"^Chapter \d{1,}"):
    global path    
    try:
        chapter = False
        header =""
        f = open(path+"res/"+generate_fname(), 'a')
        for line in lines:              
            if chapter:
                f = open(path+"res/"+generate_fname(), 'a')
                f.write(header)
            if not re.match(text_markup, line):
                if len(line.strip()) > 0:
                    f.write(line)
                chapter = False
            else:
                f.close()
                header = line
                chapter = True                

    except FileNotFoundError:
        print("Error writing file check your dir")
    finally:
        if not f.closed:
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
    
    
        









    