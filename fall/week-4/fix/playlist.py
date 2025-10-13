# Playlist Manager

playlist = ["Blinding Lights", "Levitating", "Watermelon Sugar", "Good 4 U"]
play_counts = [150, 200, 175, 120]

print("=== Music Playlist Manager ===\n")

# Display current playlist
print("Current Playlist:")
for i in range(len(playlist)):
    print(f"{i + 1}. {playlist[i]} - {play_counts[i]} plays")

print("\n--- Adding New Songs ---")

# Fix 1: Use -1 or len()-1 to access last item
new_song = "Stay"
playlist.append(new_song)
play_counts.append(0)
print(f"Added: {playlist[-1]} with {play_counts[-1]} plays")  # Fixed: use -1

print("\n--- Removing Songs ---")

# Fix 2: Use pop() to remove by index
print("Removing first song...")
removed_song = playlist.pop(0)  # Fixed: pop() removes by index
play_counts.pop(0)
print(f"Removed: {removed_song}")

print("\n--- Finding Songs ---")

# Fix 3: Check if song exists before using index()
search_song = "Circles"
if search_song in playlist:  # Fixed: check existence first
    position = playlist.index(search_song)
    print(f"{search_song} is at position {position + 1}")
else:
    print(f"{search_song} not found in playlist")

print("\n--- Sorting Playlist ---")

# Fix 4: sort() modifies in place, don't assign result
playlist.sort()  # Fixed: don't assign return value
print(f"Alphabetically sorted: {playlist}")

print("\n--- Updating Play Counts ---")

# Fix 5: Don't modify list while iterating
song_to_remove = "Levitating"
if song_to_remove in playlist:  # Fixed: remove outside of iteration
    index = playlist.index(song_to_remove)
    playlist.pop(index)
    play_counts.pop(index)
    print(f"Removed {song_to_remove}")


print("\n--- Most Played Song ---")

# Fix 6: Check if list is not empty before finding max
if len(play_counts) > 0:  # Fixed: check list is not empty
    max_plays = max(play_counts)
    most_played_index = play_counts.index(max_plays)
    print(f"Most played: {playlist[most_played_index]} with {max_plays} plays")
else:
    print("No songs in playlist")
