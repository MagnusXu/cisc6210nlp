#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:38:32 2019

@author: lordxuzhiyu
"""

import collections
from collections import *
import functools 
import operator 
import numpy as np
import nltk
import requests
import random, re
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

head = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
}

url = 'https://storm.cis.fordham.edu/~yli/data/MyShakespeare.txt'
html = requests.get(url, headers = head)
s = html.text 
s = s.lower()

def update(n, text):
    tokens = word_tokenize(text)
    ngrams = zip(*[tokens[i:] for i in range(n)])
    result = [" ".join(ngram) for ngram in ngrams]
    return result

def ngram_freq(n, gram):
    ngram = update(n, s)
    freq = ngram.count(gram)
    return freq

def generate(context, n, max_length):
    tokens = word_tokenize(context)
    tokens = tuple(tokens)
    vocab = set(tokens)
    
    ngram = update(n, s)
    
    output = []
    
    locator = random.randint(1, len(ngram))
    
    if len(tokens) < n-1:
        input = ngram[locator]
    elif len(tokens) == n-1:
        context = tuple(context.split(" "))
        prefix = ' '.join(context[-(n-1):])
        input = '%s %s' % (prefix, tokens[0])
    else:
        context = tuple(context.split(" "))
        input = context[-(n-1):]
        
    for i in range(max_length):
        counter = 0
        for word in vocab:
            gram = '%s %s' % (input, word)
            if (ngram_freq(n, gram)>counter):
                counter = ngram_freq(n, gram)
                input = gram
        output.append(input)
        input = str(input)
        input = input.split(' ', 1)[1]
        
    return output

#rr = generate(context = 'our business', n = 3, max_length = 30)
n = 3

tokens = word_tokenize(s)
ngrams = zip(*[tokens[i:] for i in range(n)])
res = [" ".join(ngram) for ngram in ngrams]


locator = random.randint(1, len(res))

ss = 'I think the best way is to split, but limit it to only one split by providing'
#s = s.split(' ', 1)[1]

context = 'our business'
max_length = 30

token = word_tokenize(ss)
#token = tuple(token)
vocab = set(tokens)

ngram = res

def prob(context, word):
    ngram = res
    fdist = nltk.FreqDist(context)
    context = tuple(context)
    
    v = set(tokens)
    
    if len(context)> 100000:
        probability = 1 / v
    elif word in fdist:
        if n == 1:
            probability = float(fdist[word]+1) / (v + len(ngram))
        else:
            probability = float(fdist[word]+1) / (v + ngram.count(context))
    else:
        probability = 1 / (v + 1)
    return probability

output = []

locator = random.randint(1, len(ngram))

if len(tokens) < n-1:
    input = ngram[locator]
elif len(tokens) == n-1:
    context = tuple(context.split(" "))
    prefix = ' '.join(context[-(n-1):])
    input = '%s %s' % (prefix, tokens[0])
else:
    context = tuple(context.split(" "))
    input = context[-(n-1):]

input = ' '.join(input)
    
for i in range(max_length):
    counter = 0
    freq_list = {}
    for word in vocab:
        gram = '%s %s' % (input, word)
        print(gram)
        freq = ngram_freq(n, gram)
        freq_list[word] = freq
        
        if (freq > counter):
            counter = freq
            input = gram
    freq_list = sorted 
    output.append(input)
    print('Counter: ', counter)
    try:
        input = input.split(' ', 1)[1]
    except: 
        continue
output = ' '.join(output)    
print(output)
