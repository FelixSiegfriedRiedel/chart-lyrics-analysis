import lyricsgenius
import numpy as np
import pandas as pd
from requests.exceptions import HTTPError, Timeout

token_file = open("genius_token.txt", "r")
token = token_file.read()
token_file.close()

genius = lyricsgenius.Genius(token, response_format='plain', timeout=5, sleep_time=0.1)
genius.verbose = False
genius.remove_section_headers = True
genius.skip_non_songs = True
genius.retries = 2


def get_lyrics(title, artist):
    try:
        song = genius.search_song(title, artist)
        if song:
            lyrics = song.lyrics.replace('\n', ' ').replace('\r', '')
            print('#', end='')
        else:
            lyrics = '!NoSong!'
            print('X', end='')

    # except HTTPError:
    #     lyrics = '!HTTPError!'
    #     print('E', end='')
    # except Timeout:
    #     lyrics = '!Timeout!'
    #     print('E', end='')
    # except TypeError:
    #     lyrics = '!TypeError!'
    #     print('E', end='')

    except:
        lyrics = '!Error!'
        print('E', end='')

    return lyrics


artist_song = pd.read_json('data/artist_song/artist_song.json')
#artist_song['lyrics'] = ''

# updates csv file every 20 entries
for i in range(0, 1281, 20):
    j = i + 20
    safe = artist_song.iloc[i:j].copy()
    safe['lyrics'] = np.vectorize(get_lyrics)(safe['song'], safe['artist'])
    artist_song['lyrics'].update(safe['lyrics'])
    artist_song.to_csv('data/lyrics/artist_song_lyrics.csv')
    # indicator showing progress
    print('\n', j, '/', 1309)

# adds the remaining lyrics
safe = artist_song.iloc[1301:].copy()
safe['lyrics'] = np.vectorize(get_lyrics)(safe['song'], safe['artist'])
artist_song['lyrics'].update(safe['lyrics'])
artist_song.to_csv('data/lyrics/artist_song_lyrics.csv', encoding='utf-16')
print('\n', 1309, '/', 1309)
print(' Done!')
