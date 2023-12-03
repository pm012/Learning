"""divide sting to lexems 

e.g. "2+ 34-5 * 3" => ['2', '+', '34', '-', '5', '*', '3']


"""

def token_parser(s):
    res = []    
    operators = ['*','-','+','/','(',')']    
    num = ""
    reset = True
    
    for i in range(len(s)):
        if reset: 
            num=""

        if s[i]==" ":            
            continue
        elif s[i] in operators:
            res.append(s[i])            
        elif s[i].isdigit():
            num +=s[i]
            reset = False
            try:                
                if not s[i+1].isdigit():
                    res.append(num)                    
                    reset = True
            except IndexError:
                res.append(num)
                break          
            
    return res


record = "(2+ 3) *4 - 5 * 3"
print(token_parser(record))





