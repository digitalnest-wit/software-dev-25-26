print("Music Library")
print("=" * 30)

total_songs = 0
total_plays = 0
favorite_song = ""
favorite_artist = ""

while True:
    print("\n1. Add a Song to Counter")
    print("2. Play a Song")
    print("3. Set Favorite Song")
    print("4. View Stats")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        print("Add a Song to Counter")
        song_name = input("Enter song name: ").strip()
        
        if song_name == "":
            # TODO: song_name should not be empty. Display an error message
            # and continue
            pass
        
        artist = input("Enter artist name: ").strip()
        
        # TODO: artist should not be empty. If artist is empty, display an
        # error message and continue
        
        total_songs += 1
        print(f"\n✓ Added '{song_name}' by {artist}")
        print(f"You now have {total_songs} songs tracked!")
    
    elif choice == "2":
        # TODO: If total_songs is 0, display a message letting the user know
        # they have no music and continue
        
        print("▶ Play a Song")
        song_name = input("Enter song name to play: ").strip()
        
        if song_name == "":
            print("\n * Error: song name cannot be empty!")
            continue
        
        print(f"\n♫ Now playing: {song_name}")
        # TODO: Update the total_plays variable (increment by one)
    
    elif choice == "3":
        print("★ Set Favorite Song")
        favorite_song = input("Enter your favorite song name: ").strip()
        
        if favorite_song == "":
            print("\n * Error: song name cannot be empty!")
            continue
        
        favorite_artist = input("Enter the artist name: ").strip()
        
        if favorite_artist == "":
            print("\n * Error: artist name cannot be empty!")
            continue
        
        print(f"\n✓ Favorite song set to '{favorite_song}' by {favorite_artist}")
    
    elif choice == "4":
        # TODO: Display total_songs, total_plays, and favorite_song and
        # favorite_artist, if a favorite song is set.
        pass
    
    elif choice == "5":
        # TODO: Display summary with total_songs and total_plays, then break
        pass
    
    else:
        print("\n * Error: invalid choice selected.")
        continue

print("\nSession terminated.")
