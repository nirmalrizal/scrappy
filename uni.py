# -*- coding: utf-8 -*-

import unicodedata

text = "nirmal   काठमाडौं । शरद भेषावकर rijal nirmal र प्रदीप                            ऐरीको अर्धशतकीय    (current)"

uni_text = unicode(text.strip(), 'utf-8')

wordlength = len(uni_text)
allTextList = []
for i in range(wordlength):
    singleWord = uni_text[i]
    nextWord = ""
    if(i+1 != wordlength):
            nextWord = uni_text[i+1]
    if 'DEVANAGARI' in unicodedata.name(singleWord) or ('SPACE' in unicodedata.name(singleWord) and 'SPACE' not in unicodedata.name(nextWord) and 'DEVANAGARI' in unicodedata.name(nextWord)):
        allTextList.append(singleWord.encode('utf-8'))

oneLineText = ''.join(allTextList).strip()

finalTextArr = oneLineText.split('।')
finalTextArr = map(lambda x : x.strip(), finalTextArr)
finalText = " ।\n".join(finalTextArr) + " ।"

file = open('news.txt', 'w')
file.write(finalText)
file.close()
    

