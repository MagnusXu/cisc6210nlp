#!/usr/bin/env python
# coding: utf-8

# ## Brown Corpus
# 
# The Brown Corpus was the first million-word electronic corpus of English, created in 1961 at Brown University.
# This corpus contains text from 500 sources, and the sources have been categorized by genre, such as news, editorial, and so on.
# 
# http://icame.uib.no/brown/bcm-los.html
# 
# The corpus could be accessed as a list of words, or a list of sentences (each sentence is a list of words).
# 
# 

# In[1]:


#from nltk.corpus import brown
import nltk
nltk.download()


# In[ ]:


from nltk.corpus import brown


# In[2]:


from nltk import bigrams, trigrams, ngrams, word_tokenize


# In[3]:


import operator
import os
import sys
import numpy as np


# In[4]:


def get_brown_sentences():
    # returns 57340 of the Brown corpus
    # each sentence is represented as a list of individual string tokens
    return brown.sents()


# In[5]:


#convert sentences of words to list of indexes of words,
#the size of vocabulary could be set to a given number.
#the number of sentences could be set to a given number

def get_sentences_with_word2idx_limit_vocab(n_vocab=2000, num=0):
    if n_vocab<=2:
        print('vocabulary size should be larger than 2')
        system.exit(0)
        
    sentences = get_brown_sentences()
    print('Finish reading brown sentences')
    
    indexed_sentences = []#save processed sentences

    #word to index mapping
    i = 2 #first two are fixed.
    word2idx = {'START': 0, 'END': 1}
    idx2word = ['START', 'END']

    #dictionary for word's index and its counts
    word_idx_count = {
        0: float('inf'), #set their counts to big to keep them on top of the sorting results later
        1: float('inf'),
    }

    #process each sentence at a time
    for sentence in sentences:
        indexed_sentence = []
        for token in sentence:
            token = token.lower()
            if token not in word2idx:#new token
                idx2word.append(token)
                word2idx[token] = i
                i += 1
                

            # keep track of counts for later sorting
            idx = word2idx[token]
            word_idx_count[idx] = word_idx_count.get(idx, 0) + 1

            indexed_sentence.append(idx)
        indexed_sentences.append(indexed_sentence)

    print('finished all sentences and build index')

    # restrict vocab size

    # set all the words I want to keep to infinity
    # so that they are included when I pick the most
    # common words
    

    sorted_word_idx_count = sorted(word_idx_count.items(), key=operator.itemgetter(1), reverse=True)
    word2idx_small = {}
    new_idx = 0
    idx_new_idx_map = {}
    for idx, count in sorted_word_idx_count[:n_vocab]:
        word = idx2word[idx]
        #print(word, count, end=" |")
        word2idx_small[word] = new_idx
        idx_new_idx_map[idx] = new_idx
        new_idx += 1
    #print(word2idx_small)
    # let 'unknown' be the last token
    word2idx_small['UNKNOWN'] = new_idx 
    unknown = new_idx

    assert('START' in word2idx_small)
    assert('END' in word2idx_small)
    
    # map old idx to new idx
    sentences_small = []
    number_s=0
    
    flag = True
    for sentence in indexed_sentences:
        
        if num == 0:
            flag = True
        elif num>0  and number_s < num:
            flag = True
        elif num >0 and number_s >= num:
            flag = False
        
        if flag == True and len(sentence) > 1:
            new_sentence = [idx_new_idx_map[idx] if idx in idx_new_idx_map else unknown for idx in sentence]
            sentences_small.append(new_sentence)
            number_s +=1

    return sentences_small, word2idx_small


# In[6]:


def get_bigram_probs(sentences, V, start_idx, end_idx, smoothing=1):
    #structure of bigram probability matrix will be
    #(last word-current word)--> probability
    #we will use add-one smoothing
    #ignore the end word
    bigram_probs=np.ones((V,V))*smoothing#size of V by V matrix, add one from the beginning
    #print(bigram_probs)
    for sentence in sentences:
        #print(len(sentence))
        for i in range(len(sentence)):
            if i==0:
                #begining word
                bigram_probs[start_idx,sentence[i]]+=1
            else:
                #middle word
                bigram_probs[sentence[i-1], sentence[i]]+=1
                
            #if we are at the final word
            #we update the bigram for last->current
            #and current-> end token
            if i == len(sentence)-1:
                #final word
                bigram_probs[sentence[i], end_idx]+=1
    #print(bigram_probs)
    #normalize the counts along the rows to get probabilities
    bigram_probs/=bigram_probs.sum(axis=1, keepdims=True)#sum per row
    #print(bigram_probs)
    return bigram_probs


# In[7]:


def get_bigram_probs_nltk(sentences, V, start_idx, end_idx, smoothing=1):
    bigram_probs = np.ones((V,V))*smoothing
    for sentence in sentences:
        bigram = list(ngrams(sentence,2))
        #print(bigram)
            
        bigram_probs[start_idx, bigram[0][0]]+=1
        bigram_probs[bigram[len(bigram)-1][1], end_idx]+=1
        for bg in bigram:
            bigram_probs[bg[0],bg[1]]+=1
    
    bigram_probs/=bigram_probs.sum(axis=1,keepdims=True)
    return bigram_probs
            


# In[ ]:





# In[ ]:




