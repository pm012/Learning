""""
create a function in python def capital_text(s): 
that will return string with the first capital letter (ignoring spaces)
 and also make captial letters that will follow '.', '!', '?' 
 ignoring any following spaces
"""

import re

def capital_text(s):
    result = ''
    capitalize_next = True

    for char in s:
        if char.isalpha():
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
        elif char in ['.', '!', '?']:
            capitalize_next = True
            result += char
        else:
            result += char

    return result


def capital_text1(s):
    res = list()
    delimiters = ['.', '?', '!']
    pattern = f"({'|'.join(map(re.escape, delimiters))})"
    sentenses=re.split(pattern,s)    
    for sentence in sentenses:
        lst = list(sentence)
        for i in range(len(lst)):
            if lst[i].isalpha():
                lst[i] = lst[i].upper()
                break
        res.append("".join(lst))
    return "".join(res)
        
            
    
    
    # for sentence in sentenses:
    #     for ch in sentence:
    #         if ch.isalpha():
    #             ch = ch.upper()
    #             continue


# Example usage:
input_text = "this is a sample text.    it has multiple sentences.    what do you think?    some text!   text."
output_text = capital_text1(input_text)
print(output_text)
# def split_with_delimiters(s, delimiters):
#     pattern = f"({'|'.join(map(re.escape, delimiters))})"
#     result = re.split(pattern, s)
#     # Filter out empty strings from the result
#     result = [part for part in result if part]
#     return result

# # Example usage:
# input_string = "Test string. Another sentence? Testing."
# delimiters = ['.', '?']

# result = split_with_delimiters(input_string, delimiters)
# print(result)
