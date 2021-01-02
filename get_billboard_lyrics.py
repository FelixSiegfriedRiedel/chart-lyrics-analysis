import lyricsgenius
import numpy as np
import pandas as pd

token_file = open("genius_token.txt", "r")
token = token_file.read()
token_file.close()

genius = lyricsgenius.Genius(token)
genius.verbose = False
genius.remove_section_headers = True

def get_lyrics(title, artist):
    song = genius.search_song(title, artist)
    if song:
        lyrics = song.lyrics.replace('\n', ' ').replace('\r', '')
        print('#', end='')
    else:
        lyrics = ''
        print('X', end='')
    return lyrics

# artist_song = pd.read_csv('output/artist_song.csv', encoding='utf8')
artist_song = pd.read_json('output/artist_song.json')
artist_song['lyrics'] = ''

# updates csv file every 20 entries
for i in range(0, 741, 20):
    j = i + 20
    safe = artist_song.iloc[i:j].copy()
    safe['lyrics'] = np.vectorize(get_lyrics)(safe['song'], safe['artist'])
    artist_song['lyrics'].update(safe['lyrics'])
    artist_song.to_csv('output/artist_song_lyrics.csv')
    # indicator showing progress
    print('\n', j, '/', 768)

# adds the remaining lyrics
safe = artist_song.iloc[761:].copy()
safe['lyrics'] = np.vectorize(get_lyrics)(safe['song'], safe['artist'])
artist_song['lyrics'].update(safe['lyrics'])
artist_song.to_csv('output/artist_song_lyrics.csv', encoding='utf-16')
print('\n', 768, '/', 768)
print(' Done!')