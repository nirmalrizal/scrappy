# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import requests
import unicodedata

website_url = "https://baahrakhari.com/news-details/169935/2018-12-19"
DEFAULT_ENCODING = "utf-8"

# Make request to the website
site_resp = requests.get(website_url)

# Change encoding of website to UTF-8
site_resp.encoding = DEFAULT_ENCODING
html_doc = site_resp.text
soup = BeautifulSoup(html_doc, 'html.parser')

body_text = soup.body.get_text().encode(DEFAULT_ENCODING)
text_list = filter(lambda x : x.strip() != "" and 'DEVANAGARI' in unicodedata.name(unicode(x.strip(), 'utf-8')[0]), body_text.splitlines())

# for line in text_list:
#         uni_text = unicode(line.strip(), 'utf-8')
#         print unicodedata.name(uni_text[0])
    

filter_text = '\n'.join(text_list)

file = open('test_1.txt', 'w')
file.write(filter_text)
file.close()