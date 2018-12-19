# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import unicodedata

website_url = "https://baahrakhari.com/news-details/169935/2018-12-19"
DEFAULT_ENCODING = "utf-8"

# Removes spaces between lines and text other that devnagari
# It checks only the first letter of the sentence if it is devnagari, this can be fixed
def removeUnwatedData(text):
    return text.strip() != "" and 'DEVANAGARI' in unicodedata.name(unicode(text.strip(), 'utf-8')[0])

# Removes spaces on front and back of the text on each line 
def removeExtraSpace(text):
    return text.strip()

# Make request to the website
site_resp = requests.get(website_url)

# Change encoding of website to UTF-8 ( Life saving trick )
site_resp.encoding = DEFAULT_ENCODING
html_doc = site_resp.text
soup = BeautifulSoup(html_doc, 'html.parser')

body_text = soup.body.get_text().encode(DEFAULT_ENCODING)
text_list = map(removeExtraSpace, filter(removeUnwatedData, body_text.splitlines()))

    
# Joins items of the list with a line break
final_text = '\n'.join(text_list)

file = open('news.txt', 'w')
file.write(final_text)
file.close()