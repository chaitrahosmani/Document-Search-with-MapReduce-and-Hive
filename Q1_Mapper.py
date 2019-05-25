#!/usr/bin/env python

import sys
import os
import re

concat_two = None
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        # get the name of the file using below command
        file_name = os.getenv('mapreduce_map_input_file')
        # remove all the leading and trailing special characters
        word = word.strip('%$.,;\'\"&|_\(\)')
        # covert all into lower characters; useful in case insensitive search
        word = word.lower()
        # create word and file_name as keyword, this helps in sorting
        if(len(word) > 0):
            concat_two = str(word) +"|"+str(file_name)
            print '%s\t%s' % (concat_two,1)