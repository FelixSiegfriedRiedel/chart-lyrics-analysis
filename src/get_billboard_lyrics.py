import lyricsgenius
import numpy as np
import pandas as pd
from requests.exceptions import HTTPError, Timeout

from progress_bar import printProgressBar


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
            lyrics = song.lyrics
            url = 'https://genius.com' + song.path
        else:
            lyrics = '!NoSong!'
            url = ''
    except:
        lyrics = '!Error!'
        url = ''

    return lyrics, url


lyrics_list = []
url_list = []

artist_song = pd.read_json('data/artist_song/artist_song.json')
length = len(artist_song)
printProgressBar(0, length, prefix='Progress:', suffix='Complete', length=50)

for i in range(0, length):
    lyrics, url = get_lyrics(artist_song['song'].iloc[i], artist_song['artist'].iloc[i])
    lyrics_list.append(lyrics)
    url_list.append(url)
    printProgressBar(i + 1, length, prefix='Progress:', suffix='Complete', length=50)

artist_song['lyrics'] = lyrics_list
artist_song['url'] = url_list

artist_song.to_csv('data/lyrics/bb-t100-lyrics.csv', encoding='utf-8')
