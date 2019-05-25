#!/usr/bin/env python

from operator import itemgetter
import sys
import math

current_word = None
current_count = 0
word = None
# Input the number of files in tennis folder
file_count=100
idf=0.00
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)
    # Referenced from Session3-Lab-MapReduce
    try:
        count = float(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # calculate the IDF
            idf = file_count/current_count
            if(idf != 0):
                idf = math.log(file_count/current_count)
            print '%s\t%.2f' % (current_word, idf)
        current_count = count
        current_word = word

if current_word == word:
    idf = file_count/current_count
    if(idf != 0):
        idf = math.log(file_count/current_count)
    print '%s\t%s' % (current_word, idf)