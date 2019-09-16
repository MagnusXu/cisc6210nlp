#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:48:19 2019

@author: lordxuzhiyu
"""

import nltk
import pandas as pd

class NGram:
    def _init_(self, n):
        self.n = n
        
    def update(self, text):
        return 0
    
    def get_vocab(self):
        return 0
    
    def size_vocab(self):
        return 0
    
    def prob(self, context, word):
        return 0
    
    def len_text(self):
        return 0
    
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
    
