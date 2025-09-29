def make_album(artist_name, album_title, songs=None):
    if songs:
        album_dictionary = {
            'artist': artist_name,
            'album': album_title,
            'songs': songs
        }
    else:
        album_dictionary = {
            'artist': artist_name,
            'album': album_title,
        }

    return album_dictionary

while True:
    print("\nPlease tell me the name of the artist and the album title: ")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Album title: ")
    if album_title == 'q':
        break

    formatted_album = make_album(artist_name, album_title)
    print(formatted_album)
