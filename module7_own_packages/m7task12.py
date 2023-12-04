"""
Function file_operations should open file on <path> and add <additional_info> 
record to the end of the file.
The file should be opened in read mode and return record starting with <start_pos> 
with length <count_chars>. Return the read line

"""


def file_operations(path, additional_info, start_pos, count_chars):
    with open(path,'a') as file:
        file.write(additional_info)

    with open(path, 'r') as file:
        #MOve the file pointer to the specified starting position
        file.seek(start_pos)

        #Read the specified number of characters
        return file.read(count_chars) 
    


# Example usage
path = "example.txt"
additional_info = "Additional information."
start_pos = 10
count_chars = 5

result = file_operations(path, additional_info, start_pos, count_chars)
print(result)