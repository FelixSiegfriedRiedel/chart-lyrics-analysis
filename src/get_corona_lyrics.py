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


corona_artists = [
    'Luke Combs', 'Bon Jovi', 'twenty one pilots', 'Pitbull', 'Turbo, Gunna and Young Thug', 'OneRepublic', 'Bono',
    'st. Pedro', 'Randy Newman', 'Adam Hambrick', 'Michael Bublé, Barenaked Ladies and Sofía Reyes',
    'Mike Love featuring John Stamos', 'Lil TJay', 'Grace Potter featuring Marcus King, Jackson Browne and Lucious',
    'Mike Campbell', 'Rodney Darkchild Jerkins Presents The Good News', 'Snow Tha Product', 'Tye Tribbett',
    'Benjamin Gibbard', 'Alexander 23', 'Drive-by Truckers', 'Erika Ender', 'Riley Green', 'SENRI OE',
    'Queen + Adam Lambert', 'Gloria Estefan', 'Avril Lavigne', 'Cardi B and iMarkkeyz', 'Todrick Hall',
    'Hillsong Young & Free', 'Alicia Keys', 'Live Lounge Allstars', 'ArtistsCAN', 'The Rolling Stones', 'Norah Jones',
    'HAIM', 'John Paul White featuring Rosanne Cash', 'Jewel', 'Brad Paisley', 'YUNGBLUD'
]

corona_songs = [
    'Six Feet Apart', 'Do What You Can', 'Level of Concern', 'I Believe That We Will Win (World Anthem)',
    'Quarantine Clean', 'Better Days', 'Let Your Love Be Known', 'Phone Sex', 'Stay Away',
    'Between Me and the End of the World', 'Gotta Be Patient', 'This Shall Too Pass', 'Ice Cold',
    'Eachother', 'Lockdown', 'Come Together', 'Nowhere to Go (Quarantine Love)', 'We Gon’ Be Alright',
    'Life in Quarantine', 'IDK You Yet', 'Quarantine Together', 'Back to the Basics', 'Better Than Me',
    'Togetherness', 'You Are the Champions', 'Put Your Mask On!', 'We Are Warriors', 'Coronavirus',
    'Mask, Gloves, Soap, Scrubs', 'A Message for My Best Friends', 'My House',
    'Times Like These (BBC Radio 1 Stay Home Live Lounge)', 'Lean on Me', 'Living In a Ghost Town',
    'Tryin’ to Keep It Together', 'I Know Alone', 'We’re All In This Together Now', 'Grateful',
    'No I In Beer', 'Weird!'
]

corona_lyrics = pd.DataFrame()

corona_lyrics['artist'] = pd.Series(corona_artists)
corona_lyrics['song'] = pd.Series(corona_songs)



lyrics_list = []
url_list = []




length = len(corona_lyrics)
printProgressBar(0, length, prefix='Progress:', suffix='Complete', length=50)

for i in range(0, length):
    lyrics, url = get_lyrics(corona_lyrics['song'].iloc[i], corona_lyrics['artist'].iloc[i])
    lyrics_list.append(lyrics)
    url_list.append(url)
    printProgressBar(i + 1, length, prefix='Progress:', suffix='Complete', length=50)

corona_lyrics['lyrics'] = lyrics_list
corona_lyrics['url'] = url_list

corona_lyrics.to_csv('../../data/lyrics/corona-lyrics.csv', encoding='utf-8')
corona_lyrics.to_excel('../../data/output/corona-lyrics.xlsx', encoding='utf-8')