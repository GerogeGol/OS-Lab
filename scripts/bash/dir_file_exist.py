#!/usr/bin/python

import sys
import os
import os.path

PATH = sys.argv[1]
TO_FIND = sys.argv[2]

flag = os.path.exists(PATH + TO_FIND)

if not flag:
