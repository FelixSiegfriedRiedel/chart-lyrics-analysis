import lyricsgenius
import pandas as pd

from progress_bar import printProgressBar


token_file = open("genius_token.txt", "r")
token = token_file.read()
token_file.close()

genius = lyricsgenius.Genius(token, response_format='plain', timeout=3, sleep_time=0.1)
genius.verbose = False
genius.remove_section_headers = True
genius.skip_non_songs = True
genius.retries = 1


def get_lyrics(url):
    try:
        lyrics = genius.lyrics(song_url=url)
    except:
        lyrics = '!Error!'
    return lyrics


lyrics_list = []
lyrics_invalid = pd.read_json('../data/lyrics/lyrics_invalid.json')
length = len(lyrics_invalid)

printProgressBar(0, length, prefix='Progress:', suffix='Complete', length=50)
for i in range(0, length):
    lyrics = get_lyrics(lyrics_invalid['url'].iloc[i])
    lyrics_list.append(lyrics)
    printProgressBar(i + 1, length, prefix='Progress:', suffix='Complete', length=50)

lyrics_invalid['lyrics'] = lyrics_list

lyrics_invalid.to_csv('data/lyrics/lyrics_invalid_updated.csv', encoding='utf-8')





