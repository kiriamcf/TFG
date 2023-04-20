import songsExtraction
import lyricsAnalyzer
import imageGeneration
import pandas as pd
import os.path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')


def generate_wordcloud(song_occurances, artist, song):
    wc = WordCloud(background_color="white", colormap="Dark2", max_font_size=100,
                   random_state=15).generate_from_frequencies(song_occurances)
    plt.figure(figsize=(20, 10))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("csv/" + "%s%s%s%s" % (artist, '-', song, '.png'))


def check_if_album_csv_exists(album_name, artist_name):
    formated_album_name = album_name.title().replace(" ", "")
    formated_artist_name = artist_name.title().replace(" ", "")
    return os.path.isfile("csv/" + formated_album_name + '-' + formated_artist_name + ".csv")


def mainOnlineArtists(artist):
    artist_dataframe = songsExtraction.get_songs_by_artist(artist)
    album_occurences = dict()
    for song, index in enumerate(artist_dataframe.index):
        song_occurences = lyricsAnalyzer.analyze_lyrics(
            artist_dataframe['lyrics'][song])
        if (index == 0):
            album_occurences = song_occurences
        else:
            album_occurences = {i: album_occurences.get(
                i, 0) + song_occurences.get(i, 0) for i in set(album_occurences).union(song_occurences)}
        # album_occurences = album_occurences + occurences
        # print(type(occurences))
        song_dataframe = pd.DataFrame.from_dict(song_occurences.items())
        song_dataframe.columns = ['words', 'occurences']
        song_dataframe.to_csv("csv/" + "%s%s%s%s" % (artist, '-',
                              artist_dataframe['title'][song], '.csv'), index=False)
        generate_wordcloud(song_occurences, artist,
                           artist_dataframe['title'][song])

    album_occurences = dict(
        sorted(album_occurences.items(), key=lambda item: item[1], reverse=True))
    print('final ->', album_occurences)
    # imageGeneration.generate512x512('Music single cover image for a song called "we all make mistakes" that talks about love and pain')


if __name__ == '__main__':
    mainOnlineArtists("Mac Miller")
    # main()
    # print(check_if_album_csv_exists("nothing is god", "kiriam campobadal"))
