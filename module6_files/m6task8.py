"""
Three is a list of applicants who passed the entrance examps to the university. Blow is the structure
of list of the applicants:

[
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

The dictionary contains name, speciality and results for mathematics, language and english


Write the data to output file as follows:

Kovalchuk Oleksiy,301,175,180,155
Ivanchuk Boryslav,101,135,150,165
Karpenko Dmitro,201,155,175,185

Requirements:
Open file output for writing using context manager of context with and 'w' mode
Use writelines or write to write data to output file
"""

#case when input data is read from file and evalueated
def save_applicant_data1(source, output):
    inpt = ""
    str = ""
    lst = []
    with open(source, 'r') as inp_file:        
        inpt = inp_file.read()
        lst = eval(inpt)    
    for dict in lst:
        str += f"{dict['name']},{dict['specialty']},{dict['math']},{dict['lang']},{dict['eng']}\n"
    str=str[0 : len(str)-1] #remove the last line return
    with open(output, 'w') as out_file:
        out_file.write(str)



#case when input is a list of dictionaries
def save_applicant_data(source, output):
    
    str=""
    for dict in source:
        str += f"{dict['name']},{dict['specialty']},{dict['math']},{dict['lang']},{dict['eng']}\n"
    str=str[0 : len(str)-1] #remove the last line return
    with open(output, 'w') as out_file:
        out_file.write(str)




inp_data = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
inp_path = "./module6_files/task8txt/inp.txt"
out_path = "./module6_files/task8txt/out1.txt"
#save_applicant_data1(inp_path, out_path)
save_applicant_data(inp_data, out_path)



    
