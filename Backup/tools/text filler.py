#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:16:43 2019

@author: lordxuzhiyu
"""

import nltk
import random

from bs4 import BeautifulSoup
import pandas as pd
import requests, re

def get_text(url, head):
    html = requests.get(url, headers = head)
    txt = html.text
    return txt

head = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
}

url = 'https://storm.cis.fordham.edu/~yli/data/MyShakespeare.txt'

result = get_text(url, head)

s = result.lower()
s1 = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = nltk.word_tokenize(s1)

tokens = tuple(tokens)

ngrams = {}
chars = 36

for i in range(len(tokens)-chars):
    seq = tokens[i:i+chars]
    #print(seq)
    if seq not in ngrams.keys():
        ngrams[seq] = []
    ngrams[seq].append(tokens[i+chars])

curr_sequence = tokens[0:chars]
output = curr_sequence

for i in range(len(ngrams)):
    if curr_sequence not in ngrams.keys():
        break
    possible_chars = ngrams[curr_sequence]
    next_char = possible_chars[random.randrange(len(possible_chars))]
    output += tuple(next_char)
    curr_sequence = output[len(output)-chars:len(output)]

print(output)

