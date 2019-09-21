#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:48:19 2019

@author: lordxuzhiyu
"""

import requests
import re, random
from nltk.tokenize import word_tokenize
from nltk import ngrams
from nltk.probability import FreqDist

class NGram:
    def _init_(self, n):
        head = {
            'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
        }
        
        url = 'https://storm.cis.fordham.edu/~yli/data/MyShakespeare.txt'
        html = requests.get(url, headers = head)
        result = html.text        
        s = result.lower()
        s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)   
        
        self.n = n
        self.text = s
        
    def update(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        tokens = word_tokenize(text)
        ngrams = zip(*[tokens[i:] for i in range(self.n)])
        result = [" .".join(ngram) for ngram in ngrams]
        return result
    
    def get_vocab(self):
        tokens = word_tokenize(self)
        return set(tokens)
    
    def size_vocab(self):
        size = len(self.get_vocab())
        return size
    
    def prob(self, context, word):
        fdist = FreqDist(context)
        if len(context)> 1000:
            probability = 1 / len(context)
        elif word in fdist:
            probability = float(fdist[word]) / len(context)
        else:
            probability = 1 / (len(context) + 1)
        return probability
    
    def len_text(self):
        tokenized_word = word_tokenize(self.s)
        return len(tokenized_word)
    
    def len_ngram(self):
        text = self.text
        gram = self.update(text)
        return len(gram)
    
    def word_freq(self, word):
        text = self.text
        tokens = word_tokenize(text)
        freq = self.prob(tokens, word)
        return freq
    
    def ngram_freq(self, gram):
        text = self.text()
        ngram = self.update(text)
        freq = self.prob(ngram, gram)
        return freq
    
    def generate_text(self, context, min_length, max_length):
        tokens = word_tokenize(context)
        gram = ngrams(tokens, self.n)
        current = tokens[0:self.n]
        output = current
        for i in range(max_length):
            possible = gram[current]
            next = possible[random.randrange(len(possible))]
            output += next
            current = output[len(output) - self.n:len(output)]
        return output
    
    def perplexity(self, text):
        per = 1
        num = 0
        s = self.text()
        gram = self.update(s)
        for word in text:
            if word in gram:
                num += 1
                probability = self.prob(gram, word)
                per = per * (1/probability)
        per = pow(per, 1/float(num))
    
        return per
