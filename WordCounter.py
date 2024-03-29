import requests
from bs4 import BeautifulSoup
import operator


def word_counter(url):
    word_list = []
    source_code = requests.get(url).text
    sasha = BeautifulSoup(source_code, 'html.parser')
    for text in sasha.find_all('span', {'class': 'text'}):
        content = text.text
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~`!@#$%^&*()_+\"-=[];',./{}|:<>?"
        for s in range(0, len(symbols)):
            word = word.replace(symbols[s], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


word_counter('http://quotes.toscrape.com/page/2/')