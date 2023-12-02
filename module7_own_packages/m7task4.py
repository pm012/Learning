"""
extend is digit()
lets consider the string is diget if it begins with +, -
ignore trailing or preceeding spaces
length should be >=1



"""

def is_integer(s):
    
    
    s=s.strip(" ")
    if len(s) == 0:
        return False
    else:
        if s[0] =='-' or s[0]=='+':
            return s[1:len(s)+1].isdigit()
        else: return s.isdigit()

print("expected True: ")
print(is_integer('123'))

print(is_integer('+123'))
print(is_integer('-123'))
#print(is_integer(123))
print(is_integer(' +123 '))
print(is_integer(' 123 '))
print("Should return false: ")
print(is_integer('   '))
print(is_integer('abc'))
#print(is_integer(True))
#print(is_integer(1.22))


    
        
    
        
    