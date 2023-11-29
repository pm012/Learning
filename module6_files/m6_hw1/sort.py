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
from pathlib import Path
import copy


root_path=""
EXTENSIONS = {
      "images": [".JPG",".JPEG",".PNG", ".SVG"],
      "videos": [".MP4",".AVI",".MKV", ".MOV"],
      "documents": [".DOCX",".PDF",".XLSX",".PPTX",".TXT",".DOC"],
      "music":['.MP3', '.OGG', '.WAV', '.AMR'],
      "archives": ['.ZIP', '.TAR', '.GZ'],
}


def normalize(file_name:str)->str:
        CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
        TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
        TRANS = {}

        for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
            TRANS[ord(c)] = l
            TRANS[ord(c.upper())] = l.upper()
        

        res = re.sub(r"(?u)[^\w.]", "_", file_name.translate(TRANS))

        
        
        return res

#process dir to check
def get_category(extension):
    for category, extensions_list in EXTENSIONS.items():
        if extension.upper() in extensions_list:
            return category
    return "unknown"

def handle_folder(folder_path):
    known_extensions = set()
    unknown_extensions = set()
    

    for path in Path(folder_path).rglob('*'):
        if path.is_file():
            _, file_extension = os.path.splitext(path)
            file_extension_upper = file_extension.upper()
            known_extensions.add(file_extension_upper)

            category = get_category(file_extension_upper)

            if category != "unknown":
                category_path = Path(root_path) / category
                category_path.mkdir(parents=True, exist_ok=True)

                if category == 'archives':
                    # Unpack the archive and move its contents to a subfolder
                    normalized = str(path.parent/normalize(path.name))
                    shutil.move(str(path.parent/path.name), normalized)
                    archive_folder = category_path / normalize(path.stem)
                    archive_folder.mkdir(exist_ok=True)
                    shutil.unpack_archive(normalized, str(archive_folder))
                    os.remove(normalized)
                else:
                    shutil.move(str(path), str(category_path / normalize(path.name)))
        elif path.is_dir() and path.name not in ['archives', 'video', 'audio', 'documents', 'images'] and root_path+"/archives"not in str(path):
            # Recursively handle subfolders
            print(path)
            handle_folder(path)
            

    # Delete empty folders
    for path in Path(folder_path).rglob('*'):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()

    return known_extensions, unknown_extensions

filenames = ["документ.doc", "my_file.txt", "Minfin.avi", "ВіДеО.mp4", "мій@mP4.mp4", "ТУт також якийсь файл.bmp", "arch.tar.gz", "файл.розшир.ение" ]

#for filename in filenames:
#     print(normalize(filename))

#f_name = "Бандерогусак для анімації (goose)-20231028T171952Z-001.zip"
#print(normalize(f_name))

#path= "./"
root_path = "/home/devel/Videos"
handle_folder(root_path)










