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
    lyrics = []
    artists = []
    needsClear = []

    artist = genius.search_artist("Mac Miller", max_songs=5, sort="popularity")
    for song in artist.songs:
        titles.append(song.title)
        lyrics.append(song.lyrics)
        artists.append(song.artist)
        if (song.lyrics.startswith("Translations")):
            needsClear.append('Yes')
            continue
        needsClear.append('No')

    df = pd.DataFrame({'title':titles,'artist':artists,'lyric':lyrics,'needsClear': needsClear})

    df.to_csv('test.csv', index=False)

    return df

def testClear():
    print('TEST CLEAR')
    testString = "TranslationsEspañolPortuguês2009 Lyrics\r\nHola bon dia234Embed"

    # Translations
    print(testString.find('\r\n'))

    # Embed
    print(testString.find('Embed'))

    while (True):
        embedStartIndex = testString.find('Embed')

        if (testString[embedStartIndex - 1].isnumeric()):
            testString = testString[0 : embedStartIndex - 1 : ] + testString[embedStartIndex : :]
        else:
            break

    testString = testString.replace('Embed', '')
    print(testString)




if __name__ == "__main__":
    main()
    testClear()