#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:12:40 2019

@author: MagnusXu
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

def combine_url(url1, url2):
    return '%s%s' % (url1, url2)

def get_text(url, head):
    html = requests.get(url, headers = head)
    txt = html.text
    return txt

head = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
}

url0 = 'https://storm.cis.fordham.edu/~yli/data/LoveOutput/'
#soup = BeautifulSoup(txt,'lxml')

table0 = pd.DataFrame(columns = ['Author', 'Title', 'Tags', 'Body', 'Link'])
#success = 0
fails = 0

for line in open('/Users/lordxuzhiyu/Desktop/valid_ip.txt'):
    url = combine_url(url0, line)
    url = url.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').strip()
    try:
        #p = requests.get(url, headers = head, timeout = 5)
        #success += 1
        html = requests.get(url,headers=head)
        txt = html.text
        #print(html)
        text = txt.splitlines()
        # Title
        title = re.findall(r'(\w+) By', text[0]) 
        # Author
        author = re.findall(r'By (.+)', text[0])
        # Tags
        tag = text[2].split(' ;')
        tag = ', '.join(tag)
        # Body
        body = text[4].replace('<br><br>', '[P]')
        body = body.replace('<br>', '[L]')
        #print(body)
        # Link
        link = re.findall(r'http.+', text[6])        
        record = {'Author': author[0], 'Title': title, 'Tags': tag, 'Body': body, 'Link': link[0]}
        temp = pd.DataFrame(record, index = [0])
        #print(record)
        table0 = table0.append(temp, ignore_index = True)
        print('Suceess')
    
    except Exception as error:
        fails += 1
        print(error)
        continue

print('Fails: ', fails)
#print(table0)
# sum of poems
print('sum of poems', len(table0.index))

# sum of different authors
sum_author = len(table0['Author'].unique().tolist())
print('sum of different authors', sum_author)
 
# author sorted
print(table0['Author'].value_counts())
       
table0.to_csv('/Users/lordxuzhiyu/Desktop/CleanOutputLoveOutput.csv', 
              index = None, header = True)
