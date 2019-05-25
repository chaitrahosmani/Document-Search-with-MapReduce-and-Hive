#!/usr/bin/env python

from operator import itemgetter
import sys
import os

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    word,count = line.split('\t', 1)

    # Referenced from Session3-Lab-MapReduce
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue


    if current_word == word:
        current_count += count
    else:
        if current_word:
            # split the keyword into word and file_name
            a,b = current_word.split("|")
            print '%s\t%s\t%s' % (a,b, current_count)
        current_count = count
        current_word = word

if current_word == word:
    # split the keyword into word and file_name
    a,b = current_word.split("|")
    print '%s\t%s\t%s' % (a,b, current_count)