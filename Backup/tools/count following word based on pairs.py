from collections import Counter, deque
from nltk.tokenize import regexp_tokenize
import pandas as pd

def grouper(iterable, length=2):
    i = iter(iterable)
    q = deque(map(next, [i] * length))
    while True:
        yield tuple(q)
        try:
            q.append(next(i))
            q.popleft()
        except StopIteration:
            break

def tokenize(text):
    return [word.lower() for word in regexp_tokenize(text, r'\w+')]

def follow_probability(word1, word2, vec):
    subvec = vec.loc[word1]
    try:
        ct = subvec.loc[word2]
    except:
        ct = 0
    return float(ct) / (subvec.sum() or 1)

text = 'This is some training text this this'
tokens = tokenize(text)
markov = list(grouper(tokens))
vec = pd.Series(Counter(markov))
