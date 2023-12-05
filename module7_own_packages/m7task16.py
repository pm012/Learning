"""
decode list ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2] to get
["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]

"""
# simple implementation of decode function
def decode_simple(data):
    result = list()
    for i in range(len(data)):
        if i%2 != 0:
            repetition = int(data[i])
            for cnt in range(repetition):
                result.append(data[i-1])
    return result

#decode using list comprehension
def decode_using_list_comprehension(input_list):
    return [elem if isinstance(elem, str) else [elem - 1, elem - 1][0] * [input_list[index - 1] for _ in range(elem - 1)]
                for index, elem in enumerate(input_list) if elem != 0]

encoded_lst=["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

#decode using recursion

def decode(data):
    if len(data)==0:
        return list()
    if type(data[0]).__name__=='str':
        rep = list()
        n = data[1]
        for _ in range(n):
            rep.insert(0, data[0])
        return rep + decode(data[2:])
    else:
        return decode(data[1:])
        




print(decode(encoded_lst))


            
    
