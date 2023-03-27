import songsExtraction
import lyricsAnaliser
import pandas as pd

def main():
    artist = 'Mac Miller'
    artist_dataframe = songsExtraction.get_songs_by_artist(artist)
    for song in artist_dataframe.index:
        occurences = lyricsAnaliser.analyze_lyrics(artist_dataframe['lyrics'][song])
        song_dataframe = pd.DataFrame.from_dict(occurences)
        song_dataframe.columns = ['words', 'occurences']
        song_dataframe.to_csv("%s%s%s%s"%(artist, '-', artist_dataframe['title'][song], '.csv'), index=False)

if __name__ == '__main__':
    main()