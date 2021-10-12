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

def get_genius_resources(genius_id):
    result_dict = {}
    try:
        song = genius.song(genius_id)['song']
        result_dict['primary_artist'] = song['primary_artist']['name']
        result_dict['description'] = song['description']['plain']
        result_dict['annotations'] = genius.song_annotations(genius_id)
        result_dict['comments'] = []
        for comment in genius.song_comments(genius_id, per_page=20)['comments']:
            result_dict['comments'].append(comment['body']['plain'])
        result_dict['release_date'] = song['release_date']
    except:
        result_dict['primary_artist'] = ''
        result_dict['description'] = ''
        result_dict['annotations'] = []
        result_dict['comments'] = []
        result_dict['release_date'] = ''
    return result_dict


primary_artist_list = []
description_list = []
annotations_list = []
comments_list = []
release_date_list = []

lyrics = pd.read_csv('../data/lyrics/bb_t100_lyrics_en.csv', encoding='utf-8', index_col=0)
length = len(lyrics)

printProgressBar(0, length, prefix='Progress:', suffix='Complete', length=50)
for i in range(0, length):
    resources = get_genius_resources(lyrics['genius_id'].iloc[i])
    print(resources)
    primary_artist_list.append(resources['primary_artist'])
    description_list.append(resources['description'])
    annotations_list.append(resources['annotations'])
    comments_list.append(resources['comments'])
    release_date_list.append((resources['release_date']))
    printProgressBar(i + 1, length, prefix='Progress:', suffix='Complete', length=50)

lyrics['genius_primary_artist'] = primary_artist_list
lyrics['genius_description'] = description_list
lyrics['genius_annotations'] = annotations_list
lyrics['genius_comments'] = comments_list
lyrics['release_date'] = release_date_list
lyrics.to_csv('../data/lyrics/bb_t100_lyrics_en_v2.csv', encoding='utf-8')
lyrics.to_excel('../data/output/bb_t100_lyrics_en_v2.xlsx')
