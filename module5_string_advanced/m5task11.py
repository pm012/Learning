"""

Create a function find_all_words that is searching word matches in a text. 
The function returns list of all occurences of word in parameter 'word' in a text in case insensetive mode (e.g. pYthoN, python, PYTHon). Hence,  the   the letters sequence should be adhered.

Hint: Functions re can have another paramether <flags> and we can define case insensitivity, giving to it 
value re.IGNORECASE
"""


import re

def find_all_words(text, word):

    pattern = r'\b'+str(word)+r'\b'    
    words = re.findall(pattern, text, re.IGNORECASE)
    print(words)
    return words


find_all_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', 'Python') 