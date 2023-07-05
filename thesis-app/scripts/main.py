import songsExtraction
import lyricsAnalyzer
import imageGeneration
import pandas as pd
import os.path
import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.style.use('grayscale')


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

        song_dataframe = pd.DataFrame.from_dict(song_occurences.items())
        song_dataframe.columns = ['words', 'occurences']
        song_dataframe.to_csv("csv/" + "%s%s%s%s" % (artist, '-',
                              artist_dataframe['title'][song], '.csv'), index=False)
        generate_wordcloud(song_occurences, artist,
                           artist_dataframe['title'][song])

    album_occurences = dict(
        sorted(album_occurences.items(), key=lambda item: item[1], reverse=True))
    imageGeneration.generate512x512(
        'Music single cover image for a song called "we all make mistakes" that talks about love and pain')


def mainCustomSong(artist, song_name, genre, lyrics, resolution):
    song_occurences = lyricsAnalyzer.analyze_lyrics(lyrics)
    topic_words = []
    for i in range(len(song_occurences)):
        if i > 2:
            break
        topic_words.append(list(song_occurences)[i])

    prompt = "Music single cover image for a {} song called {} that talks about {}. The artist is called {}".format(
        genre, song_name, ", ".join(topic_words), artist)

    if resolution == '512':
        image_name = imageGeneration.generate512x512(prompt)
    elif resolution == '768':
        image_name = imageGeneration.generate768x768(prompt)

    print(image_name)


def mainCustomAlbum(artist, album_name, genre, lyrics, resolution):
    song_occurences = lyricsAnalyzer.analyze_lyrics(lyrics)
    topic_words = []
    for i in range(len(song_occurences)):
        if i > 2:
            break
        topic_words.append(list(song_occurences)[i])

    prompt = "Music cover image for a {} album called {} that talks about {}. The artist is called {}".format(
        genre, album_name, ", ".join(topic_words), artist)

    if resolution == '512':
        image_name = imageGeneration.generate512x512(prompt)
    elif resolution == '768':
        image_name = imageGeneration.generate768x768(prompt)

    print(image_name)


if __name__ == "__main__":
    if (len(sys.argv) < 7):
        print('Not enough arguments provided')
    else:
        artist = sys.argv[2]
        name = sys.argv[3]
        genre = sys.argv[4]
        lyrics = sys.argv[5]
        resolution = sys.argv[6]

        if (sys.argv[1] == "album"):
            mainCustomAlbum(artist, name, genre, lyrics, resolution)
        elif (sys.argv[1] == "song"):
            mainCustomSong(artist, name, genre, lyrics, resolution)
        else:
            print("Something went wrong with the arguments provided")
