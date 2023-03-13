import api
from lyricsgenius import Genius
import pandas as pd
# import string

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords

def get_songs_by_artist(artist):
    genius = Genius(api.genius_access_token)
    genius.remove_section_headers = True
    genius.skip_non_songs = True
    genius.retries = 10

    titles = []
    lyrics = []
    artists = []

    artist = genius.search_artist(artist, max_songs=5, sort="popularity")
    for song in artist.songs:
        titles.append(song.title)
        artists.append(song.artist)

        if (song.lyrics.startswith("Translations")):
            song.lyrics = clear_translations(song.lyrics)

        song.lyrics = clear_embed(song.lyrics)

        lyrics.append(song.lyrics)

    df = pd.DataFrame({'title':titles,'artist':artists,'lyric':lyrics})

    df.to_csv(artist+'.csv', index=False)

    return df

def clear_translations(lyrics):
    return lyrics[lyrics.find('\n')+1 : len(lyrics)]

def clear_embed(lyrics):
    while (True):
        embed_index = lyrics.find('Embed')
        if (lyrics[embed_index - 1].isnumeric()):
            lyrics = lyrics[0 : embed_index - 1 : ] + lyrics[embed_index : :]
        else:
            break

    return lyrics.replace('Embed', '')