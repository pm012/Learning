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

def normalize(file_name:str)->str:
    
    
    return ""


