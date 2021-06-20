from nltk.corpus import stopwords
from nltk import word_tokenize, FreqDist
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer

import string
import re

import pandas as pd


import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn as sns

from wordcloud import WordCloud, ImageColorGenerator

lemmatizer = WordNetLemmatizer()


def get_eng_stopwords_list(added_words_list=None):
    ''' Get the basic list of English stops words, plus punctuation, and empty text signifiers '''
    # Get English stopwords, punctuation, and 'empty text' signifiers (like empty quotes and ...)
    the_list = stopwords.words('english')  + list(string.punctuation) + ["''", '""', '...', '``']
    if added_words_list:
        the_list = stopwords.words('english')  + list(string.punctuation) + ["''", '""', '...', '``'] + added_words_list
    return the_list

def tokenize_lemmatize_text(text):
    ''' Tokenize then Lemmatize the given text '''
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tokens = tweet_tokenizer.tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens


def tokenize_text(text):
    ''' Tokenize the given text '''
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tokens = tweet_tokenizer.tokenize(text)
    return tokens


def process_text(text, stopwords_list):
    ''' Tweet prep for word cloud. Tokenize the given tweet, remove stopwords and use ascii encoding'''
    #tokenize, lowercase each token, remove stopwords
    stopwords_removed = ''
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tokens = tweet_tokenizer.tokenize(text)
    stopwords_removed = [token for token in tokens if token not in stopwords_list]
    lemmatized_tokens = [lemmatizer.lemmatize(tok) for tok in stopwords_removed]

    return lemmatized_tokens


def plot_word_cloud(text, word_max, bg_color='black'):
    ''' Plot a word cloud from the given text '''
    cloud = WordCloud(background_color=bg_color, 
                            min_word_length=3,
                            collocation_threshold = 4, 
                            max_words=word_max)
    cloud.generate(text)
    
    # plot it
    plt.figure(figsize=(15,10))
    plt.imshow(cloud, interpolation='bilinear') 
    plt.axis("off")
    plt.show()
