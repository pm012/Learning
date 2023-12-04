"""
Read the contents of the source_file and write each line to the output file with line number before the file
Record count should start with 0
example of output file
      0: record1
      1: record2
"""

def to_indexed(source_file, output_file):
    lst = list()
    with open(source_file, 'r') as input_file:
        lst = input_file.readlines()

    with open(output_file,'w') as output_file:
        for i in range(len(lst)):
            output_file.write(f"{i}: {lst[i]}")


inp_f = "./module7_own_packages/professions.txt"
out_f = "./module7_own_packages/professions_num.txt"
to_indexed(inp_f, out_f)
        
