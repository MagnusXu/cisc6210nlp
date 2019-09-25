#!/usr/bin/env python
# coding: utf-8

# The implementation of Language Model with Logistic Regression
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime

import brown


# In[2]:


def softmax(a):
    a = a-a.max() # to avoid numerical overflow
    exp_a = np.exp(a)
    return exp_a/exp_a.sum(axis=1, keepdims=True)


# In[11]:


def main():
   
   sentences, word2idx = brown.get_sentences_with_word2idx_limit_vocab(2000,20000)
   #sentences, word2idx = brown.get_sentences_with_word2idx_limit_vocab(10,10)
   V = len(word2idx)
   print(f"word total: {V}")
   start_idx= word2idx['START']
   end_idx = word2idx['END']
   print(f'Start index={start_idx} and End index = {end_idx}')
   
   #train a logistic model
   W = np.random.randn(V,V)/np.sqrt(V) #initial random values to W of shape V x V
   #print(f'W\n{W}')
   
   losses=[]
   epochs = 1
   lr = 1e-2

   
   t0=datetime.now()
   for epoch in range(epochs):
       print(f"In iteration NO.{epoch}")
       #suffle sentences each epoch
       random.shuffle(sentences) 
       
       j=0 #sentence counter
       for sentence in sentences:
           #convert sentence into one-hot coded inputs and targets
           sentence=[start_idx]+sentence+[end_idx]
           #print(sentence)
           n = len(sentence)
           print(f"Length of sentence {n}")
           
           inputs = np.zeros((n-1,V))
           targets = np.zeros((n-1,V))
           inputs[np.arange(n-1), sentence[:n-1]]=1#the sentence itself, ignoring the end index, shape n-1 x V
           targets[np.arange(n-1), sentence[1:]]=1#the next word of the target, shape n-1 x V
           # one-hot encoding of word vectors         
           #print (f'inputs:\n{inputs.shape}')
           #print(f'targets:\n{targets.shape}')
           
           #get output prediction
           predictions = softmax(inputs.dot(W)) #shape n-1 x V
           #print(f"Shape of predictions after softmax {predictions.shape}")#one for each word in the sentence
           #print(f"predictions:\n{predictions}")
           #do a gradient descent step
           W = W - lr*inputs.T.dot(predictions-targets)
           
           #keep track of the loss - cross entropy cost function            
           loss = -np.sum(targets*np.log(predictions))/(n-1)#array multiplication
           losses.append(loss)
           
           '''
           #keep track of the bigram loss
           #only do it for the first epoch to avoid redundancy
           if epoch ==0:
               bigram_predictions = softmax(inputs.dot(W_bigram))
               bigram_loss = -np.sum(targets*np.log(bigram_predictions))/(n-1)
               bigram_losses.append(bigram_loss)
           '''                
           if j%1000==0:
               print(f"epoch: {epoch}, sentence: {j}/{len(sentences)}, loss: {loss}")
           
           j+=1
           
           if j== 2:
               break
       print(f"Elapsed time training: {datetime.now()-t0}")
       plt.plot(losses)
  
       '''
       #plot a horizontal line for the bigram loss
       avg_bigram_loss=np.mean(bigram_losses)
       print('avg_bigram_loss', avg_bigram_loss)
       plt.axhline(y=avg_bigram_loss, color='r', linestyle='-')
       '''        
       #plot a smoothed losses line to reduce variability
       def smoothed_loss(x, decay=0.99):
           y = np.zeros(len(x))
           last=0
           for t in range(len(x)):
               z = decay*last+ (1-decay)*x[t]
               y[t]= z/(1-decay**(t+1))
               last = z
           return y
       
       plt.plot(smoothed_loss(losses))
       plt.show()


# In[12]:


if __name__ == '__main__':
    main()


# In[ ]:




