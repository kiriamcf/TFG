import string

import nltk
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
# from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer


def split_word(word):
    return list(word)

def is_not_punctuation(char):
    # create a set of all the punctuations (!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~)
    punctuations = set(string.punctuation)
    # check if character is existant on that set
    return (char not in punctuations)

def remove_punctuations(word_char_list):
    # for each char in word, remove it if it is punctuation
    return ''.join(list(filter(is_not_punctuation, word_char_list)))

def remove_stopwords(word):
    # create a set of all the stopwords in the english alphabet ('the', 'a', 'an', 'in'...)
    english_stopwords = set(stopwords.words('english'))
    # check if the word is existant on that set
    return (word not in english_stopwords)

def lemmatize_words(word):
    # create an instance of the nltk lemmatizer (transform words into their corresponding lemmas)
    lemma = WordNetLemmatizer()
    # lemmatize word
    return (lemma.lemmatize(word))

def count_occurences(word_list):
    occurance_dict = dict()
    for current_word in word_list:
        occurance_dict[current_word] = word_list.count(current_word)
    # list without duplicates -> list(occurance_dict.keys())
    return occurance_dict

def analyze_lyrics(lyrics):
    # test_string = "!This is_ a tests/ for the lyrics analyser! Some other words are: churches, churchs, dogs, women, women"
    # print('original -> ',test_string)
    # split the string into words
    lyrics_list_words = lyrics.lower().split()
    # split the words into characters
    lyrics_list_characters = list(map(split_word, lyrics_list_words))
    # remove the punctuations
    result = list(map(remove_punctuations, lyrics_list_characters))
    # remove the stopwords
    result = list(filter(remove_stopwords, result))
    # lemmatize the words
    result = list(map(lemmatize_words, result))
    # remove duplicate words and indicate occurrances
    result = count_occurences(result)
    # print('occurences -> ', result)
    return result



if __name__ == '__main__':
    analyze_lyrics()
    # analyze_lyrics(dataframe)
    # a partir del dataframe seleccionar la columna dels lyrics, i passar aixo als filtres