#!/usr/bin/python3

# find ./ -xdev -type f | xargs ls -ltrh | awk '{print $9,$5}'

import os


def list_files():
    '''
    Lists files along with their sizes
    '''
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            file_name = os.path.join(root, name)
            file_size = os.path.getsize(file_name)
            print (file_name, file_size)
        for name in dirs:
            directory_name = os.path.join(root, name)
            directory_size = os.path.getsize(directory_name)
            print(directory_name, directory_size)


if __name__ == "__main__":
    list_files()
