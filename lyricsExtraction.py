import api
from lyricsgenius import Genius
import pandas as pd
# import string

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords

def main():
    genius = Genius(api.genius_access_token)
    genius.remove_section_headers = True
    genius.skip_non_songs = False

    titles = []
    artists = []
    lyrics = []
    albums = []
    publishedYears = []

    artist = genius.search_artist("Andy Shauf", max_songs=3, sort="popularity")
    song = artist.song("To You")
    artist.save_lyrics()

if __name__ == "__main__":
    main()