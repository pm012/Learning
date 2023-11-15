"""
Create a function find_word that gets 2 parameters:
the first <text> and the second is <word>. Function searches <word> in a 
<text> using <search> function.
The call:
print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))


Result:
{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}




"""

import re
import json


def find_word(text, word):
    res = re.search(word, text)    
    return json.dumps({'result': bool(res), 'fist_index': res.span()[0], 'last_index': res.span()[1], 'search_sting': res.string, 'string': res.group()}, indent = 4)

    

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))