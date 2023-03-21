import songsExtraction
import lyricsAnaliser

def main():
    dataframe = songsExtraction.get_songs_by_artist('Mac Miller')
    for song_lyrics in dataframe['lyrics'].values:
        occurences = lyricsAnaliser.analyze_lyrics(song_lyrics)
        # dataframe['words'] = [occurences]
        print([occurences])

    dataframe.to_csv("Mac Miller2.csv", index=False)

if __name__ == '__main__':
    main()