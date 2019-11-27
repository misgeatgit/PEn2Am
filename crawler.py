# -*- coding: latin-1 -*-
'''
This script automates the task of crawling amharic words with their 
respective frequency in web corpuses

Output Example 

=====================
ነው 260338
ላይ 174891
ውስጥ 80072
እና 77266
ወደ 75254
=====================
'''


__author__ = 'yididiya.yilma@gmail.com'


from bs4 import BeautifulSoup
import urllib
from string import ascii_letters

OUT_FILE = 'data/dictionary.txt' 
BASE_URL = ('https://corpora.fi.muni.cz/habit/run.cgi/wordlist?corpname='
            'amwac16&refs=&wlmaxitems=1000&wlsort=f&subcnorm=freq&corpnamed'
            '=amwac16&reload=&wlattr=word&usengrams=0&ngrams_n=2&ngrams_max_n'
            '=2&nest_ngrams=0&wlpat=&wlminfreq=1&wlmaxfreq=0&wlfile=&wlblacklist'
            '=&wlnums=frq&wltype=simple&wlpage')
NUM_PAGES = 1000
LINE_CACHE_SIZE = 41666666 # nearly 1GB assuming each line takes 24 bytes
english_alphabet = list(ascii_letters)



if __name__ == '__main__':
    with open(OUT_FILE, 'a') as f:
        lines_cached = ''
        lines_count = 0
        for i in range(NUM_PAGES):
            print('Crawling page - {}'.format(i + 1))
            url = '{}={}'.format(BASE_URL, i + 1)
            if i == 0:
              print(url)
            response = urllib.urlopen(url)
            response = response.read()
            soap = BeautifulSoup(response, 'html')
            rows = []
            if soap.table:
               rows = soap.table.find_all('tr')[1:]
            # print(len(rows))
            if not len(rows):
                break

            for row in rows:
                word, frequency = row.find_all('td')
                if len(list(filter(lambda x: x in word.text, english_alphabet))):
                    continue
                lines_cached +=  '{} {}\n'.format(word.text.encode('utf-8').strip(),
                                               int(frequency.text))
                lines_count += 1
                if lines_count >= LINE_CACHE_SIZE:
                    f.write(lines_cached)
                    #clear cache and reset counter
                    lines_cached = ''
                    lines_count = 0
        # Flush the last remaining cache content
        f.write(lines_cached)
