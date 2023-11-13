'''
Create dictionary TRANS with the help of 'zip' function  outside the translate function.
The written 'tranlsate' function 
    * Gets a string and returns a string
    * Transliterates the incoming cyrylic string to lathin 

    Example: 
        print(translate("Дмитро Короб"))  # Dmitro Korob
        print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk

Note:
During creation of TRANS dictionary, sourcecode TRANS[ord(c.upper())] = l.title() will be considered as incorrect, 
and TRANS[ord(c.upper())] = l.upper()  - correct. It's because if all leters in documents are in upper case - all name is printed in capital letters

'''

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

print(TRANS)
    
    


def translate(name):

    return name.translate(TRANS)
    

print(translate("Дмитро Короб"))
#translate("Олекса Івасюк")
translate("Серґій Бабкін")
#translate("КАТЕРИНА Крошка")



    
    