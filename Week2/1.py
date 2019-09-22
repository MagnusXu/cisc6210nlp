#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:48:19 2019

@author: lordxuzhiyu
"""

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
#s = s.lower()
#s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)

class NGram:

    
    def _init_(self, n, text):          
        head = {
            'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
        }
        
        url = 'https://storm.cis.fordham.edu/~yli/data/MyShakespeare.txt'
        html = requests.get(url, headers = head)
        s = html.text         
        
        self.n = n
        self.text = s
        
    def update(self, text):
        if self.n == 2:
            text = '. ' + text
        elif self.n == 3:
            text = '. '*2 + text
        else:
            tokens = word_tokenize(text)
            ngrams = zip(*[tokens[i:] for i in range(self.n)])
            result = [" ".join(ngram) for ngram in ngrams]
        return result
    
    def get_vocab(self):
        tokens = word_tokenize(s)
        return set(tokens)
    
    def size_vocab(self):
        size = len(self.get_vocab())
        return size
    
    def prob(self, context, word):
        ngram = self.update(s)
        fdist = FreqDist(context)
        context = tuple(context)
        
        v = self.size_vocab()
        
        if len(context)> 100000:
            probability = 1 / v
        elif word in fdist:
            if self.n == 1:
                probability = float(fdist[word]+1) / (v + len(ngram))
            else:
                probability = float(fdist[word]+1) / (v + ngram.count(context))
        else:
            probability = 1 / (v + 1)
        return probability
    
    def len_text(self):
        tokenized_word = word_tokenize(s)
        return len(tokenized_word)
    
    def len_ngram(self):
        gram = self.update(s)
        return len(gram)
    
    def word_freq(self, word):
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
        tokens = word_tokenize(s)
        freq = tokens.count(word) / len(tokens)
        return freq
    
    def ngram_freq(self, gram):
        ngram = self.update(s)
        freq = self.prob(ngram, gram)
        return freq
    
    def generate_text(self, context, min_length, max_length):
        tokens = word_tokenize(context)
        tokens = tuple(tokens)
        
        gram = {}
        
        for i in range(len(tokens) - max_length):
            seq = tokens[i:i + max_length]
            #print(seq)
            if seq not in gram.keys():
                gram[seq] = []
            gram[seq].append(tokens[i + max_length])
        
        curr_sequence = tokens[0:max_length]
        output = curr_sequence
        
        for i in range(max_length):
            if curr_sequence not in gram.keys():
                break
            possible_chars = gram[curr_sequence]
            next_char = possible_chars[random.randrange(len(possible_chars))]
            output += tuple(next_char)
            curr_sequence = output[len(output) - max_length:len(output)]

        return output
    
    def perplexity(self, text):
        per = 1
        num = 0
        gram = self.update(s)
        for word in text:
            if word in gram:
                num += 1
                probability = self.prob(gram, word)
                per = per * (1/probability)
        per = pow(per, 1/float(num))
    
        return per
