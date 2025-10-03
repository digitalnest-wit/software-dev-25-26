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
            print("\n * Error: song name cannot be empty!")
            continue
        
        artist = input("Enter artist name: ").strip()
        
        if artist == "":
            print("\n *Error: artist name cannot be empty!")
            continue
        
        total_songs += 1
        print(f"\n✓ Added '{song_name}' by {artist}")
        print(f"You now have {total_songs} songs tracked!")
    
    elif choice == "2":
        if total_songs == 0:
            print("\nYou haven't added any songs yet!")
            continue
        
        print("▶ Play a Song")
        song_name = input("Enter song name to play: ").strip()
        
        if song_name == "":
            print("\n * Error: song name cannot be empty!")
            continue
        
        print(f"\n♫ Now playing: {song_name}")
        total_plays += 1
    
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
        print("\nStatistics:")
        print(f"  Total songs added: {total_songs}")
        print(f"  Total plays: {total_plays}")
        
        if favorite_song == "":
            print(f"  Favorite song: Not set yet")
        else:
            print(f"  Favorite song: {favorite_song} by {favorite_artist}")
    
    elif choice == "5":
        print(f"\nSummary:")
        print(f"  Songs tracked: {total_songs}")
        print(f"  Total plays: {total_plays}")
        break
    
    else:
        print("\n * Error: invalid choice selected.")
        continue

print("\nSession terminated.")
