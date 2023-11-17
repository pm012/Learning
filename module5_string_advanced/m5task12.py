"""
Use function sub of re module to replace all stop-words from the provided list <spam_words>.
Replace all <spam_words> in <text> with asterisk '*'. 
Width of the pattern should be the same as length of the stop_word. 
Define case insensitivity of stop_words

"""


import re



#
def replace_spam_words(text, spam_words):
    pattern = r"|".join(spam_words)

    p = re.sub(pattern, repl  , text, flags = re.IGNORECASE)
    return p

def repl(m):
    return '*' * len(m.group())

#another implementation without repl function
def replace_spam_words1(text, spam_words):
    pattern = r"|".join(spam_words)

    p = re.sub(pattern, lambda m : '*' * len(m.group())  , text, flags = re.IGNORECASE)
    return p



   
text = 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn '
stop_words_list = ["the", "python"]

print(replace_spam_words(text, stop_words_list))
print(replace_spam_words1(text, stop_words_list))

