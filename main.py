import songsExtraction
import lyricsAnaliser
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

def generate_wordcloud(occurances, artist, song):
    occurances_dict = dict()
    for (word, occurance) in occurances:
        occurances_dict[word] = occurance[0]
    wc = WordCloud(background_color="white",colormap="Dark2",max_font_size=100,random_state=15).generate_from_frequencies(occurances_dict)
    plt.figure(figsize=(20,10))
    plt.imshow(wc,interpolation="bilinear")
    plt.axis("off")
    plt.savefig("%s%s%s%s"%(artist, '-', song, '.png'))

def main():
    artist = 'Mac Miller'
    artist_dataframe = songsExtraction.get_songs_by_artist(artist)
    for song in artist_dataframe.index:
        occurences = lyricsAnaliser.analyze_lyrics(artist_dataframe['lyrics'][song])
        song_dataframe = pd.DataFrame.from_dict(occurences)
        song_dataframe.columns = ['words', 'occurences']
        song_dataframe.to_csv("%s%s%s%s"%(artist, '-', artist_dataframe['title'][song], '.csv'), index=False)
        generate_wordcloud(occurences, artist, artist_dataframe['title'][song])

if __name__ == '__main__':
    main()