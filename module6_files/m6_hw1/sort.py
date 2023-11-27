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
import shutil

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
      #dir_list = os.listdir(dir_path)
      #print(dir_list)
      for dirpath, _, filenames in os.walk(dir_path):
            for f in filenames:
                  print(os.path.join(dirpath, f))

#process dir to check
def get_category(extension):
    for category, extensions_list in EXTENSIONS.items():
        if extension.upper() in extensions_list:
            return category
    return "unknown"

def sort_files_by_extension(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                _, file_extension = os.path.splitext(file)
                category = get_category(file_extension.upper())
                if category != "unknown":
                    category_path = os.path.join(directory, category)
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    shutil.move(file_path, os.path.join(category_path, file))

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                os.rmdir(dir_path)
            except OSError:
                pass  # Directory not empty

filenames = ["документ.doc", "my_file.txt", "Minfin.avi", "ВіДеО.mp4", "мій@mP4.mp4", "ТУт також якийсь файл.bmp", "arch.tar.gz", "файл.розшир.ение" ]

#for filename in filenames:
#     print(normalize(filename))

path= "./"
process_dir(path)









