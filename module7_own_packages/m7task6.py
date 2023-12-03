"""
Implement function solve_riddle(riddle, word_length, start_letter, reverse=False)
to find a word that is located in the riddle string.
Params:
1. riddle - string that contains word
2. word_length - searched word length
3. start_letter - letter from which begins the searched word
4. reverse - defines the direction in which the word is written. 
For example if reverse = True 'mi1rewopret' will contain the word 'power'

Function should return searched word. By default in direct order. If the word 
is not found it should be returned empty string.
"""

import re
def solve_riddle(riddle, word_length, start_letter, reverse=False):
    pattern = rf"{start_letter}\w{{{word_length-1}}}"
    res = list()
    if not reverse:        
        res = re.findall(pattern, riddle)        
    else:
        reverse_riddle = riddle[::-1]
        res =  re.findall(pattern, reverse_riddle)
    if len(res) > 0:
        return res[0]
    else: return ""
    


puzzle = "abcpowerqwer"
puzzle1 = "qwertyrewopwer"
puzzle3 ="ablaskdjlakj"
print(solve_riddle(puzzle3,5, "p", reverse=True))
