#!/usr/bin/python

import sys
import os
import os.path
PATH  = sys.argv[1]
FIND = sys.argv[2]

os.chdir(PATH)
os.path.exists()
print(PATH, FIND)