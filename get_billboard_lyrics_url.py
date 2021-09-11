import lyricsgenius
import pandas as pd

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


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
lyrics_invalid = pd.read_json('data/artist_song/lyrics_invalid.json')
length = len(lyrics_invalid)

printProgressBar(0, length, prefix='Progress:', suffix='Complete', length=50)
for i in range(0, length):
    lyrics = get_lyrics(lyrics_invalid['url'].iloc[i])
    lyrics_list.append(lyrics)
    printProgressBar(i + 1, length, prefix='Progress:', suffix='Complete', length=50)

lyrics_invalid['lyrics'] = lyrics_list

lyrics_invalid.to_csv('data/lyrics/lyrics_invalid_updated.csv', encoding='utf-8')





