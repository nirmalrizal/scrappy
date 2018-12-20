# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import unicodedata
import os

DEFAULT_ENCODING = "utf-8"

# Removes spaces on front and back of the text on each line
def removeExtraSpace(text):
    return text.strip()

def makeFilePath(rawUrl):
        urlArr = rawUrl.split("//")[1].split("/")
        urlArr[-1] = urlArr[-1].split(".")[0] + ".csv"
        filePath = "/".join(urlArr)
        return filePath

def scrapWebsiteAndSaveData(website_url):
        print "\nFetching from : " + website_url

        # Make request to the website
        site_resp = requests.get(website_url)

        # Change encoding of website to UTF-8 ( Life saving trick )
        site_resp.encoding = DEFAULT_ENCODING
        html_doc = site_resp.text
        soup = BeautifulSoup(html_doc, 'html.parser')

        body_text = soup.body.get_text().encode(DEFAULT_ENCODING)
        text_list = map(removeExtraSpace, body_text.splitlines())

        
        # # Joins items of the list with a line break
        intermediate_filtered_text = ' '.join(text_list)

        uni_text = unicode(intermediate_filtered_text.strip(), DEFAULT_ENCODING)

        wordlength = len(uni_text)
        allTextList = []
        for i in range(wordlength):
                singleWord = uni_text[i]
                nextWord = ""
                if(i+1 != wordlength):
                        nextWord = uni_text[i+1]
                if 'DEVANAGARI' in unicodedata.name(singleWord) or ('SPACE' in unicodedata.name(singleWord) and 'SPACE' not in unicodedata.name(nextWord) and 'DEVANAGARI' in unicodedata.name(nextWord)):
                        allTextList.append(singleWord.encode(DEFAULT_ENCODING))

        oneLineText = ''.join(allTextList).strip()

        # Split text based on Purnabiram and merge them on separate lines
        finalTextArr = oneLineText.split('।')
        finalTextArr = map(removeExtraSpace, finalTextArr)
        finalText = "Sentences,\n" + " ।,\n".join(finalTextArr) + " ।"

        # Check and make path for the file
        abs_file_path = "data/" + makeFilePath(website_url)
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, abs_file_path)
        if not os.path.exists(os.path.dirname(file_path)):
                os.makedirs(os.path.dirname(file_path))

        # Save scraped data on some file
        file = open(file_path, 'w')
        file.write(finalText)
        file.close()
        print "File saved on : " + abs_file_path

urlList = [
        "https://www.onlinekhabar.com/2018/12/728298",
        "http://www.imnepal.com/quotes-nepali-language",
        "http://radiokantipur.ekantipur.com/news/2018-12-20/20181220101216.html",
        "https://baahrakhari.com/news-details/170003/2018-12-20",
        "http://annapurnapost.com/news/115646"
]

for url in urlList:
        scrapWebsiteAndSaveData(url)