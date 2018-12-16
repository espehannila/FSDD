# -*- coding: utf-8 -*-
# Stopwords module
import os

fname                   = 'stopwords.txt'
this_file               = os.path.abspath(__file__)
this_dir                = os.path.dirname(this_file)
wanted_file             = os.path.join(this_dir, fname)

def remove(str):        # remove stopwords from given string using stopwords.txt file
    cachedStopWords     = set()

    file                = open(wanted_file,'r')
    words               = [l.strip('\n') for l in file.readlines()]
    
    cachedStopWords.update(words)

    new_str = ' '.join([word for word in str.split() if word not in cachedStopWords])
    return new_str