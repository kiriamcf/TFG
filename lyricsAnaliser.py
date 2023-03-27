import string

import nltk
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
# from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer


def split_word(word):
    return list(word)

def is_not_punctuation(char):
    # create a set of all the punctuations (!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~)
    punctuations = set(string.punctuation)
    # check if character is existent on that set
    return (char not in punctuations)

def remove_punctuations(word_char_list):
    # for each char in word, remove it if it is punctuation
    return ''.join(list(filter(is_not_punctuation, word_char_list)))

def remove_stopwords(word):
    # create a set of all the stopwords in the English alphabet
    english_stopwords = set(stopwords.words('english'))
    # check if the word is existent on that set
    return (word not in english_stopwords)

def lemmatize_words(word_tuple):
    # word_tuple = (word, POS)
    # create an instance of the nltk lemmatizer (transform words into their corresponding lemmas)
    lemma = WordNetLemmatizer()
    tag = lemmatize_pos_tagger(word_tuple[1])
    if tag is None:
        return word_tuple[0]
    # lemmatize word
    return (lemma.lemmatize(word_tuple[0], tag))

def lemmatize_pos_tagger(nltk_tag):
    # Assign the proper pos (part of speech) to each word
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def count_occurences(word_list):
    occurance_dict = dict()
    for current_word in word_list:
        occurance_dict[current_word] = [word_list.count(current_word)]
    # order the list in ascending order
    occurance_dict = sorted(occurance_dict.items(), key=lambda x: x[1], reverse=True)
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

def analyse_lyrics_test():
    test_string = "!This is_ a tests/ for the lyrics analyser! Some other words are: churches, churchs, dogs, women, woman, love, loving, loves, loved"
    lyrics_list_words = test_string.lower().split()
    lyrics_list_characters = list(map(split_word, lyrics_list_words))
    result = list(map(remove_punctuations, lyrics_list_characters))
    result = list(filter(remove_stopwords, result))
    result = nltk.pos_tag(result)
    result = list(map(lemmatize_words, result))
    result = count_occurences(result)
    print('occurences -> ', result)

if __name__ == '__main__':
    # analyze_lyrics()
    # analyze_lyrics(dataframe)
    # a partir del dataframe seleccionar la columna dels lyrics, i passar aixo als filtres
    analyse_lyrics_test()