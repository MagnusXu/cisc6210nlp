#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:11:28 2019
@author: MagnusXu
"""

import pandas as pd
import re
import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 

clean = pd.read_csv('/Users/lordxuzhiyu/Desktop/CleanOutputLoveOutput.csv')

df1 = pd.DataFrame(columns = ['PoemID', 'Author', 'Body', 'Length', 'UniCount'])
df2 = pd.DataFrame(columns = ['PoemID', 'Author', 'Body', 'Length', 'UniCount'])
df3 = pd.DataFrame(columns = ['PoemID', 'Author', 'Body', 'Length', 'UniCount'])

for index, row in clean.iterrows():
    print(index)
    poemID = index
    author = row['Author']
    
    tokens = word_tokenize(row['Body'])
    body1 = ' '.join(tokens)
    len1 = len(tokens)
    uni1 = len(set(tokens))
    
    clean_tokens = list()
    sr = stopwords.words('english')
    for token in tokens:
        if not token in sr:
            clean_tokens.append(token)
    body2 = ' '.join(clean_tokens)
    len2 = len(clean_tokens)
    uni2 = len(set(clean_tokens))
    
    tab3 = []
    ps = PorterStemmer() 
    stems = clean_tokens
    for w in stems:
        w = ps.stem(w)
        tab3.append(w)
    body3 = ' '.join(tab3)
    len3 = len(tab3)
    uni3 = len(set(tab3))   
    
    raw1 = {'PoemID': poemID, 'Author': author, 'Body': body1,
            'Length': len1, 'UniCount': uni1}
    record1 = pd.DataFrame(raw1, index = [0])
    df1 = df1.append(record1, ignore_index = True)
    
    raw2 = {'PoemID': poemID, 'Author': author, 'Body': body2,
            'Length': len2, 'UniCount': uni2}
    record2 = pd.DataFrame(raw2, index = [0])
    df2 = df2.append(record2, ignore_index = True)
    
    raw3 = {'PoemID': poemID, 'Author': author, 'Body': body3,
            'Length': len3, 'UniCount': uni3}
    record3 = pd.DataFrame(raw3, index = [0])
    df3 = df1.append(record3, ignore_index = True)

df1.to_csv('/Users/lordxuzhiyu/Desktop/ProcessedLoveOutput1.csv', 
              index = None, header = True)  
df2.to_csv('/Users/lordxuzhiyu/Desktop/ProcessedLoveOutput2.csv', 
              index = None, header = True)  
df3.to_csv('/Users/lordxuzhiyu/Desktop/ProcessedLoveOutput3.csv', 
              index = None, header = True)    
