""""
implement function create_backup(path, file_name, employee_residence)
Where:
<path> - file path
<file_name> - filename
<employee_residence> - dictionary username: country e.g. {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}


Function should perform following:
1. Create binary file <file_name> with path <path>
2. Save data from the dictionary  to the file. Each new record should be "key value", e.g. "Michael Canada"
3. Archive filder on <path> using shutil
4. Name of the archive should be <backup_folder.zip>
5. Function should return path to the archive <backup_folder.zip>

Requirements:
* Write contains of the employee_residence dictionary to binary file with name <file_name> to folder <path> using <with> operator
* use symbol / to split <path> and <file_name>
* To the end of each record "Michael Canada" should be followed by '\n'
* Saved data should be encoded using method <encode>
* For writing records use method <write>
* Arhive should be in .zip format and should have name 'backup_folder'. And it should be created using make_archive

"""

import shutil


def create_backup(path, file_name, employee_residence):
    pass