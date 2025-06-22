def add_album(library, album_info):
    artist, title, year, songs = album_info
    library[title] = (artist, year, songs)
    return library


def create_playlist(library, song_selections):
    playlist = []
    for album_title, song_name in song_selections:
        if album_title in library:
            _, _, songs = library[album_title]
            if song_name in songs:
                playlist.append(song_name)
    return playlist


def add_song_to_album(library, album_title, new_song):
    if album_title in library:
        artist, year, songs = library[album_title]
        if new_song not in songs:
            songs.append(new_song)
        library[album_title] = (artist, year, songs)
    return library


def remove_song_from_playlist(playlist, song):
    if song in playlist:
        playlist.remove(song)
    return playlist


def list_unique_artists_and_genres(library, genre_map):
    unique_artists = set()
    unique_genres = set()
    for album_title, (artist, _, _) in library.items():
        unique_artists.add(artist)
        if album_title in genre_map:
            unique_genres.add(genre_map[album_title])
    return unique_artists, unique_genres


library = {}
playlist = []
genre_map = {}

while True:
    print("\n===== Music Library Menu =====")
    print("1. Add a new album")
    print("2. Create a playlist")
    print("3. Add a song to an album")
    print("4. Remove a song from the playlist")
    print("5. Show library")
    print("6. Show playlist")
    print("7. Show unique artists and genres")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        artist = input("Enter artist name: ")
        title = input("Enter album title: ")
        year = int(input("Enter release year: "))
        songs = input("Enter songs (comma-separated): ").split(",")
        songs = [song.strip() for song in songs]
        genre = input("Enter album genre: ")
        album_info = (artist, title, year, songs)
        library = add_album(library, album_info)
        genre_map[title] = genre
        print("Album added successfully.")

    elif choice == "2":
        song_selections = []
        print("Enter song selections from different albums.")
        while True:
            album_title = input("Album title (or type 'done' to finish): ")
            if album_title.lower() == "done":
                break
            song_name = input("Song name: ")
            song_selections.append((album_title, song_name))
        playlist = create_playlist(library, song_selections)
        print("Playlist created successfully.")

    elif choice == "3":
        album_title = input("Enter album title to add a song to: ")
        new_song = input("Enter new song name: ")
        library = add_song_to_album(library, album_title, new_song)
        print("Song added to album.")

    elif choice == "4":
        song = input("Enter the song to remove from playlist: ")
        playlist = remove_song_from_playlist(playlist, song)
        print("Song removed from playlist.")

    elif choice == "5":
        print("\n--- Music Library ---")
        for title, (artist, year, songs) in library.items():
            print(f"Album: {title} | Artist: {artist} | Year: {year} | Songs: {songs}")

    elif choice == "6":
        print("\n--- Playlist ---")
        print(playlist)

    elif choice == "7":
        artists, genres = list_unique_artists_and_genres(library, genre_map)
        print(f"Unique Artists: {artists}")
        print(f"Unique Genres: {genres}")

    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
