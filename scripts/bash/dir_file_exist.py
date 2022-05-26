#!/usr/bin/python

import sys
import os
import os.path

PATH = sys.argv[1]
PATH_TO_FIND = sys.argv[2]

PATH = os.path.expanduser(PATH) + "/"

PATH_TO_FIND_L = PATH_TO_FIND.split("/")
PATH += "/".join(PATH_TO_FIND_L[:-1])
TO_FIND = PATH_TO_FIND_L[-1]

ldir = os.listdir(PATH)

for el in ldir:
    if TO_FIND in el:
        if os.path.isdir(PATH + "/" + el):
            print("It's directory")

        if os.path.isfile(PATH + "/" + el):
            print("It's file")

        print(f"Absolute path: {os.path.abspath(PATH + '/' + TO_FIND)}")
        exit(0)
else:
    print("No such file or directory")
