""""
Create a program to sort files in a specified folder (e.g rubish) by category.
Program should be called from command line with a command: <python sort.py /home/Documents/rubish>
 - Create a separate function to move here folder processing
 - Script should be able to call itself to be able to process folders on any level (function should recurcively call itself to process 
 included subfolders)

 Sample of categories by extension (letters after the period in filename):
 - images ('JPEG', 'PNG', 'JPG', 'SVG');
 - videos ('AVI', 'MP4', 'MOV', 'MKV');
 - documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
 - music ('MP3', 'OGG', 'WAV', 'AMR');
 - archives ('ZIP', 'GZ', 'TAR');
 

All files and folders should be renamed deleting all symbols that could cause the issues.
For this purpose you can apply function <normalize>.
Files should be renamed in a way to change only filename (but not file extension)

Function normalize:
1. Transliterates cyrrilic alphabet to lathin
2. Changes all symbols, except lathin and numbers to '_'

Requirements to normalize function:
 - takes filename as a sting and returns normalized filename as a sting
 - transliterates cyrrilic symbols to lathin ones
 - changes all symbols, except lathin letters and digits to symbol '_'
 - transliteration should be readable
 - The case of the letters should be adhered (lower case letters should remain lower case, upper case letter should be transliterated as capital letters)

 Requirements to the task:
 - All files should be renamed with <normalize> function
 - extension of the files should not be changed
 - empty folders should be deleted
 - script should ignore folders archives, audio, documents, images;
 - unpacked contents of the arhive should be moved to folder <archives> to the subfolder with the same name as unpacked archive(without extension)
 - files with unknown extension should be left without changes
 
 """

import re
import os

EXTENSIONS = {
      "images": [".JPG",".JPEG",".PNG", ".SVG"],
      "videos": [".MP4",".AVI",".MKV", ".MOV"],
      "documents": [".DOCX",".PDF",".XLSX",".PPTX",".TXT",".DOC"],
      "music":['.MP3', '.OGG', '.WAV', '.AMR'],
      "archives": ['.ZIP', '.TAR', '.GZ']


}


def normalize(file_name:str)->str:
        CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
        TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
        TRANS = {}

        for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
            TRANS[ord(c)] = l
            TRANS[ord(c.upper())] = l.upper()
        

        res = re.sub(r"(?u)[^-\w.]", "_", file_name.translate(TRANS))

        
        
        return res

def process_dir(dir_path):
      dir_list = os.listdir(dir_path)
      
      
      pass





filenames = ["документ.doc", "my_file.txt", "Minfin.avi", "ВіДеО.mp4", "мій@mP4.mp4", "ТУт також якийсь файл.bmp", "arch.tar.gz", "файл.розшир.ение" ]

for filename in filenames:
     print(normalize(filename))






