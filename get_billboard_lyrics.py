import lyricsgenius
import numpy as np
import pandas as pd
from requests.exceptions import HTTPError, Timeout

token_file = open("genius_token.txt", "r")
token = token_file.read()
token_file.close()

genius = lyricsgenius.Genius(token, response_format='plain', timeout=3, sleep_time=0.1)
genius.verbose = False
genius.remove_section_headers = True
genius.skip_non_songs = True
genius.retries = 1

def get_lyrics(title, artist):
    try:
        song = genius.search_song(title, artist)
        if song:
            lyrics = song.lyrics.replace('\n', ' ').replace('\r', '')
            print('#', end='')
        else:
            lyrics = '!NoSong!'
            print('X', end='')
    except:
        lyrics = '!Error!'
        print('E', end='')

    return lyrics


artist_song = pd.read_json('data/artist_song/artist_song.json')
artist_song['lyrics'] = ''

# updates csv file every 20 entries
for i in range(0, 1301, 20):
    j = i + 20
    safe = artist_song.iloc[i:j].copy()
    safe['lyrics'] = np.vectorize(get_lyrics)(safe['song'], safe['first_artist'])
    artist_song['lyrics'].update(safe['lyrics'])
    artist_song.to_csv('data/lyrics/artist_song_lyrics.csv')
    # indicator showing progress
    print('\n', j, '/', 1322)

# adds the remaining lyrics
safe = artist_song.iloc[1321:].copy()
safe['lyrics'] = np.vectorize(get_lyrics)(safe['song'], safe['first_artist'])
artist_song['lyrics'].update(safe['lyrics'])
artist_song.to_csv('data/lyrics/artist_song_lyrics.csv', encoding='utf-8')
print('\n', 1322, '/', 1322)
print(' Done!')
