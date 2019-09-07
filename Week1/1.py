import requests
from bs4 import BeautifulSoup
import re

def get_soup(url):
    html = requests.get(url)
    txt = html.text
    soup = BeautifulSoup(txt, 'lxml')
    return soup

def get_link(url):
    soup = get_soup(url)
    text = soup.findAll('table')[0].findAll('td')
    rows = []
    for x in text:
        rows.append(str(x))
    valid = []
    for row in rows:
        pattern = '<a href=.+</a>'
        pattern1 = '".+"'
        result0 = re.search(pattern, row)
        result = re.search(pattern1, result0)
        if result:
            link = result.group(0)
            link = link.strip('"')
            valid.append(link)
    return valid
            
url = 'https://storm.cis.fordham.edu/~yli/data/LoveOutput/'
valid = get_link(url)
print(valid)
with open('/Users/lordxuzhiyu/Desktop/valid_ip.txt', 'a') as f:
    for item in valid:
        f.write("%s\n" % item)
