#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:48:19 2019

@author: lordxuzhiyu
"""

import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

class NGram:
    def _init_(self, n):
        self.n = n
        
    def update(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        tokens = [token for token in text.split(" ") if token != ""]
        ngrams = zip(*[tokens[i:] for i in range(self.n)])
        return [" ".join(ngram) for ngram in ngrams]
    
    def get_vocab(self):
        tokens = nltk.word_tokenize(self)
        return set(tokens)
    
    def size_vocab(self):
        size = len(self.get_vocab())
        return size
    
    def prob(self, context, word):
        tokens = word_tokenize(context)
        fdist = FreqDist(tokens)
        if len(tokens)> 1000:
            probability = 1 / len(tokens)
        elif word in fdist:
            probability = float(fdist[word]) / len(tokens)
        else:
            probability = 1 / (len(tokens) + 1)
        return probability
    
    def len_text(self):
        tokenized_word = word_tokenize(self)
        return len(tokenized_word)
    
    def len_ngram(self):
        return 0
    
    def word_freq(self, word):
        return 0
    
    def ngram_freq(self, gram):
        return 0
    
    def generate_text(self, context, min_length, max_length):
        return 0
    
    def perplexity(self, text):
        return 0
    
