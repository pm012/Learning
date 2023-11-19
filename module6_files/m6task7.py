"""
Write data from input file to output file removing all digits.
- Use 'with' for both for input and output file
- Use 'r' mode for input file  and 'w' for output file
- Write to result to output file using 1 write session

"""

import re

def sanitize_file(source, output):
    pattern = r"\d{1,}"
    str= ""
    with open(source, 'r') as source_file:
        for record in source_file:
            str += re.sub(pattern, "", record )    
    with open(output, 'w') as output_file:
        output_file.write(str)


path_inp = "./module6_files/task7txt/inp.txt"
path_out = "./module6_files/task7txt/out.txt"

sanitize_file(path_inp, path_out)

