#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:48:19 2019

@author: lordxuzhiyu
"""

import re, random
from nltk.tokenize import word_tokenize
from nltk import ngrams
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
        tokens = word_tokenize(self)
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
        return len(self) - self.n + 1
    
    def word_freq(self, word):
        freq = self.prob(self, word)
        return freq
    
    def ngram_freq(self, gram):
        tokens = ngrams(self.split(), self.n)
        fdist = FreqDist(tokens)
        if gram in fdist:
            freq = float(fdist[gram]) / len(tokens)
        else:
            freq = 1 / (len(tokens) + 1)
        return freq
    
    def generate_text(self, context, min_length, max_length):
        tokens = word_tokenize(context)
        gram = ngrams(tokens, self.n)
        current = tokens[0:self.n]
        output = current
        for i in range(min_length, max_length):
            possible = gram[current]
            next = possible[random.randrange(len(possible))]
            output += next
            current = output[len(output) - self.n:len(output)]
        return output
    
    def perplexity(self, text):
        return pow(2.0, self.entropy(text))
