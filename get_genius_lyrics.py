import lyricsgenius
token_file = open("genius_token.txt", "r")
token = token_file.read()
token_file.close()

genius = lyricsgenius.Genius(token)

artist = genius.search_artist("Andy Shauf", max_songs=1)
song = genius.search_song("To You", "Andy Shauf")
artist.add_song(song)
print(artist)