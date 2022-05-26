#!/usr/bin/python
import os
import sys

FILE_NAME = sys.argv[1]
if not os.path.exists(FILE_NAME):
    print("No such file or directory")
    exit(-1)

if os.access(FILE_NAME, os.R_OK):
    print("Read", end=" ")
if os.access(FILE_NAME, os.W_OK):
    print("Write", end=" ")
if os.access(FILE_NAME, os.X_OK):
    print("Execute", end=" ")
print()
