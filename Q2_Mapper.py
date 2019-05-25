#!/usr/bin/env python

import sys
import os

for line in sys.stdin:
    line = line.strip()
    words, file_name, count = line.split()
    # output the word which is present across documents
    # this word will be counted in reducer
    print '%s\t%s' % (words, 1)