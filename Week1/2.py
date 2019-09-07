#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:57:32 2019

@author: MagnusXu
"""

import pandas as pd
import re
from nltk import word_tokenize
from nltk import sent_tokenize

clean = pd.read_csv('/Users/lordxuzhiyu/Desktop/CleanOutputLoveOutput.csv')

df = pd.DataFrame(columns = ['PoemID', 'Author', 'LengthOne', 'LengthTwo',
                             'NumLine', 'NumPara', 'NumSent', 'NumComma'])

for index, row in clean.iterrows():
    print(index)
    poemID = index
    author = row['Author']
    
    tokens = tokens = word_tokenize(row['Body'])
    len1 = len(set(tokens))
    
    nonPunct = re.compile('.*[A-Za-z0-9].*')
    tokens2 = [w for w in tokens if nonPunct.match(w)]
    len2 = len(set(tokens2))
    
    p = row['Body'].count('[P]')
    l = row['Body'].count('[L]')
    numL = l + p
    numP = p
    
    sen = sent_tokenize(row['Body'])
    comma = row['Body'].count(',')
    
    raw = {'PoemID': poemID, 'Author': author, 'LengthOne': len1,
              'LengthTwo': len2, 'NumLine': numL, 'NumPara': numP, 
              'NumSent':len(sen), 'NumComma': comma}
    record = pd.DataFrame(raw, index = [0])
    
    df = df.append(record, ignore_index = True)

df.to_csv('/Users/lordxuzhiyu/Desktop/ProcessedLoveOutput0.csv', 
              index = None, header = True)    
