import requests
from bs4 import BeautifulSoup as bs
import random, re

head = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
}

positive_url = 'https://storm.cis.fordham.edu/~yli/data/electronics/positive.review'
negative_url = 'https://storm.cis.fordham.edu/~yli/data/electronics/negative.review'

good_html = requests.get(positive_url, headers = head)
bad_html = requests.get(negative_url, headers = head)
good_review = good_html.text  
bad_review = bad_html.text  

soup = bs(good_review, 'lxml')
text = soup.find_all('review_text')
s = [l.text for l in text]



print(' ', s)
