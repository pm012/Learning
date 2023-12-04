
def repeat(k:str, n:int)->str:
    n=n+1
    rpt_str =""
    if n==1:
        return k
    elif n>1: 
        for _ in range(n):
            rpt_str += k
        return rpt_str
    


def sequence_buttons(string):
    res=""
    char_dict = {
        '1': ['.', ',', '?', '!', ':'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z'],
        '0': [' ']
        }
    for ch in string:        
        for k,v in char_dict.items():
            if ch.isalpha() and ch.upper() in v:                    
                res+=repeat(k,v.index(ch.upper()))
            elif not ch.isalpha() and ch in v:
                res+=repeat(k,v.index(ch))
            else:
                continue

    return res

#more eficient implementation
def sequence_buttons1(string):
    res = ""
    char_dict = {
        '1': ['.', ',', '?', '!', ':'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z'],
        '0': [' ']
    }

    for ch in string:
        for k, v in char_dict.items():
            if ch.upper() in v:
                res += k * (v.index(ch.upper()) + 1)

    return res
            


print(sequence_buttons1("Hello, World!"))
