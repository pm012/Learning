"""
write function encode(data) to encode list
["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ] or string  "XXXZZXXYYYZZ"
the function should return list:
["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

"""

def encode(data):
    lst = list()    
    if len(data) == 0:
        return list()
    if type(data).__name__ == "str":
        lst = [*data]
    elif type(data).__name__=="list":
        lst = data
    else:
        print("Incorrect data provided")
        return result
    n = range(1, len(lst))
    rpt=1
    for cnt in n:
        if lst[cnt]==lst[cnt-1]:
            rpt+=1
        else: 
            break
    return [lst[0], rpt]+encode(lst[rpt:])



    
str1 = "XXXZZXXYYYZZ"
lst1 = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]
result = encode(str1)
print(result)

result1 = encode(lst1)
print(result1)




