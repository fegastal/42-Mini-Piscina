#!/usr/bin/python3

from local_lib.path import Path

def my_program():

    try:
        Path.mkdir("folder")
        Path.touch('folder/file')
        file = Path('folder/file')
        file.write_lines(['Hello World!'])
        print(file.read_text())
    except FileExistsError as exception:
        print(exception)

if __name__ == '__main__':
    my_program()