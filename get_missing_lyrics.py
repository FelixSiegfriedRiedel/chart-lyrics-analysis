import lyricsgenius
import numpy as np
import pandas as pd
from requests.exceptions import HTTPError, Timeout

token_file = open("genius_token.txt", "r")
token = token_file.read()
token_file.close()

genius = lyricsgenius.Genius(token, response_format='plain', timeout=5, sleep_time=0.1)
genius.remove_section_headers = True
genius.skip_non_songs = True
genius.retries = 1

lyrics_links = [
    'https://genius.com/Ariana-grande-ghostin-lyrics',
    'https://genius.com/Ariana-grande-thank-u-next-lyrics',
    '',
    'https://genius.com/Billie-eilish-ocean-eyes-lyrics',
    'https://genius.com/Bing-crosby-and-the-andrews-sisters-mele-kalikimaka-lyrics',
    'https://genius.com/Chris-brown-no-guidance-lyrics',
    'https://genius.com/Dj-khaled-wish-wish-lyrics',
    'https://genius.com/Diplo-heartless-lyrics',
    'https://genius.com/Drake-laugh-now-cry-later-lyrics',
    'https://genius.com/J-cole-t-h-e-c-l-i-m-b-b-a-c-k-lyrics',
    'https://genius.com/John-lennon-and-yoko-ono-happy-xmas-war-is-over-lyrics',
    'https://genius.com/Keith-urban-and-p-nk-one-too-many-lyrics',
    'https://genius.com/Lil-mosey-blueberry-faygo-lyrics',
    'https://genius.com/Lil-nas-x-old-town-road-lyrics',
    'https://genius.com/Mariah-carey-all-i-want-for-christmas-is-you-lyrics',
    'https://genius.com/Migos-give-no-fxk-lyrics',
    'https://genius.com/Perry-como-its-beginning-to-look-a-lot-like-christmas-lyrics',
    'https://genius.com/Pop-smoke-tunnel-vision-outro-lyrics',
    'https://genius.com/Pop-smoke-diana-lyrics',
    'https://genius.com/Pop-smoke-for-the-night-lyrics',
    'https://genius.com/Pop-smoke-aim-for-the-moon-lyrics',
    'https://genius.com/Pop-smoke-creature-lyrics',
    'https://genius.com/Popp-hunna-adderall-corvette-corvette-lyrics',
    'https://genius.com/Post-malone-allergic-lyrics',
    'https://genius.com/Post-malone-better-now-lyrics',
    'https://genius.com/Post-malone-saint-tropez-lyrics',
    'https://genius.com/Rod-wave-the-greatest-lyrics',
    'https://genius.com/Rod-wave-rags2riches-lyrics',
    'https://genius.com/Roddy-ricch-start-wit-me-lyrics',
    'https://genius.com/Shawn-mendes-and-camila-cabello-senorita-lyrics',
    'https://genius.com/Sheck-wes-mo-bamba-lyrics',
    'https://genius.com/Summer-walker-playing-games-lyrics',
    'https://genius.com/Taylor-swift-cardigan-lyrics',
    'https://genius.com/Taylor-swift-dorothea-lyrics',
    'https://genius.com/The-weeknd-blinding-lights-lyrics',
    'https://genius.com/The-weeknd-scared-to-live-lyrics',
    'https://genius.com/Travis-scott-goosebumps-lyrics',
    'https://genius.com/Travis-scott-sicko-mode-lyrics',
    'https://genius.com/Wham-last-christmas-lyrics',
    'https://genius.com/J-hope-chicken-noodle-soup-lyrics',
    'https://genius.com/Pop-smoke-snitching-lyrics',
    'https://genius.com/Bing-crosby-ill-be-home-for-christmas-if-only-in-my-dreams-lyrics',
    '',
    'https://genius.com/Lil-durk-the-voice-lyrics',
    'https://genius.com/Ariana-grande-34-35-lyrics',
    'https://genius.com/Blake-shelton-nobody-but-you-lyrics',
    'https://genius.com/Drake-how-bout-now-lyrics',
    'https://genius.com/Ellie-goulding-and-diplo-close-to-me-lyrics',
    'https://genius.com/Internet-money-lemonade-lyrics',
    'https://genius.com/Kane-brown-swae-lee-and-khalid-be-like-that-lyrics',
    'https://genius.com/Khalid-and-john-mayer-outta-my-head-lyrics',
    'https://genius.com/The-kid-laroi-fck-you-goodbye-lyrics',
    'https://genius.com/Why-dont-we-fallin-adrenaline-lyrics',
    'https://genius.com/Xxxtentacion-and-lil-pump-arms-around-you-lyrics'

]

def get_lyrics_by_url(url):
    try:
        lyrics = genius.lyrics(song_url=url).replace('\n', ' ').replace('\r', '')
        print('#', end='')
    except:
        lyrics = '!Error!'
        print('E', end='')
    return lyrics

print(get_lyrics_by_url('https://genius.com/Kid-cudi-beautiful-trip-lyrics'))
# missing_lyrics = pd.read_excel('data/lyrics/missing_lyrics.xlsx')
# missing_lyrics.reset_index(drop=True, inplace=True)
# missing_lyrics['lyrics'] = ''
#
# for i in range(0, 21, 20):
#     j = i + 20
#     safe = missing_lyrics.iloc[i:j].copy()
#     safe['lyrics'] = np.vectorize(get_lyrics_by_url)(safe['link'])
#     missing_lyrics['lyrics'].update(safe['lyrics'])
#     missing_lyrics.to_csv('data/lyrics/missing_lyrics.csv')
#     # indicator showing progress
#     print('\n', j, '/', 56)
#
# safe = missing_lyrics.iloc[41:].copy()
# safe['lyrics'] = np.vectorize(get_lyrics_by_url)(safe['link'])
# missing_lyrics['lyrics'].update(safe['lyrics'])
# missing_lyrics.to_csv('data/lyrics/missing_lyrics.csv')
# print('\n', 56, '/', 56)
# print(' Done!')




