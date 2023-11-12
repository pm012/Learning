"""
Check spam in email or filter forbidden words in a message.

The is_spam_words function gets string <text> and checks it is containing forbidden words in a list <spam_words>
and returns True if at least one forbidden word present and False if there are no such words in text.

Words in a <text> parameter can have random register, so <is_spam_words> is registry independent and all text 
should be converted to lower case. Let's simplify that the row has only one forbidden word.

Foreseen the third parameter of the function <space_around> which should be equal Fasle by defalt.
It is responsible for searching separate word or substring. Let's consider that separate word is a word when
to the left site is located ' ' or it is located at the begining of the  text and on the right is located ' ' or '.'.

For example, if we search "rainbow" then we'll have the following for the word "rain":

<<< print(is_spam_words("We saw a rainbow.", ["rain"])) # True
<<< print(is_spam_words("We saw a rainbow.", ["rain"], True)) #False

So, in the second case the word is not sparate and is substing of another word.

And following example will have True in both cases:
<<<print(is_span_words("Rain, rain go away.", ["rain"])) #True
<<<print(is_span_words("Rain, rain go away.", ["rain"], True)) #True

"""

import re

def is_spam_words(text, spam_words, space_around=False):    

    if space_around:
        for i in spam_words:
            if text.lower().find(i.lower()):
                return True        
    else:
        text1 = text.lower().split(" ")        
        for i in text1:
            for j in spam_words:
                if (i == j.lower()) or (i==j.lower()+"."):
                    return True

        
    return False
            



    




#words = ["Sell", "buy", "Dude"]
#print(is_spam_words("Hey dude.", words))
print(is_spam_words('You’re decent, but you seem like a mismatch.', ['match']))
#pattern = re.compile(r"^?dude/s+/.")









