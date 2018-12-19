# -*- coding: utf-8 -*-

import unicodedata

name = "गृह पृष्ठ पृष्ठ"
# text_list = name.split(" ")
# for t in text_list:
#     tx = list(t)
#     for b in tx:
#         print b.encode('utf-8')
#         uni_text = unicode(b, 'utf-8')
#         print uni_text.encode('utf-8')
    # print unicodedata.name(uni_text)

uni_text = unicode(name, 'utf-8')
print unicodedata.name(uni_text[0])
    
