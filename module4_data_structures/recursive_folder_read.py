"""
Create several paths and read folders recursively and without recursion
"""


import sys
from pathlib import Path

folder_path = Path(sys.argv[1])

def parse_folder(path):
    for elements in path.iterdir():
        if elements.is_dir():
            print(f"parse folder: This is folder - {elements.name}")
        if elements.is_file():
            print(f"parse file: This is file - {elements.name}")

def parse_folder_recursion(path):
    for elements in path.iterdir():
        if elements.is_dir():
            parse_folder_recursion(elements)
        else:
            print(f"parse file: This is file - {elements.name}")

if __name__ == '__main__':
    parse_folder(folder_path)
    parse_folder_recursion(folder_path)