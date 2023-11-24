"""
Create functionality for unpacking the archive.
Create import shutil
Create a  function unpack(archive_path, path_to_unpack) that will call method unpack_arhive of the pakage shutil and
will un unpack archive to the path <path_to_unpack>
function should not return anything
"""

import shutil

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)



archive = "./backup_folder.zip"
unpack_to = "./module6_files/m6_task14_unpack/"
unpack(archive, unpack_to)



    
    

