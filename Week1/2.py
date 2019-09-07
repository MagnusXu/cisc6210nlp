import pandas as pd
import re
from nltk import word_tokenize
from nltk import sent_tokenize

clean = pd.read_csv('/Users/lordxuzhiyu/Desktop/CleanOutputLoveOutput.csv')

df = pd.DataFrame(columns = ['PoemID', 'Author', 'LengthOne', 'LengthTwo',
                             'NumLine', 'NumPara', 'NumSent', 'NumComma'])

for index, row in clean.iterrows():
    poemID = index
    author = row['Author']
    
    tokens = tokens = word_tokenize(row['Body'])
    len1 = len(set(tokens))
    
    nonPunct = re.compile('.*[A-Za-z0-9].*')
    tokens2 = [w for w in tokens if nonPunct.match(w)]
    len2 = len(set(tokens2))
    
    p = row['Body'].count('[P]')
    l = row['Body'].count('[L]')
    numL = l + p
    numP = p
    
    sen = sent_tokenize(row['Body'])
    comma = row['Body'].count(',')
