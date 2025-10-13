# Playlist Manager
# This program has multiple list-related bugs to debug

playlist = ["Blinding Lights", "Levitating", "Watermelon Sugar", "Good 4 U"]
play_counts = [150, 200, 175, 120]

print("=== Music Playlist Manager ===\n")

# Display current playlist
print("Current Playlist:")
for i in range(len(playlist)):
    print(f"{i + 1}. {playlist[i]} - {play_counts[i]} plays")

print("\n--- Adding New Songs ---")

# Bug 1: IndexError when accessing newly added song
new_song = "Stay"
playlist.append(new_song)
play_counts.append(0)
print(f"Added: {playlist[5]} with {play_counts[5]} plays")

print("\n--- Removing Songs ---")

# Bug 2: Using wrong method to remove by position
print("Removing first song...")
removed_song = playlist.remove(0)
play_counts.remove(0)
print(f"Removed: {removed_song}")

print("\n--- Finding Songs ---")

# Bug 3: Not checking if song exists before searching
search_song = "Circles"
position = playlist.index(search_song)
print(f"{search_song} is at position {position + 1}")

print("\n--- Sorting Playlist ---")

# Bug 4: Assigning result of in-place sort
sorted_playlist = playlist.sort()
print(f"Alphabetically sorted: {sorted_playlist}")

print("\n--- Updating Play Counts ---")

# Bug 5: Modifying list while iterating
for song in playlist:
    if song == "Levitating":
        playlist.remove(song)
        play_counts.pop(1)

print("\n--- Most Played Song ---")

# Bug 6: Trying to find max without checking if list is empty
max_plays = max(play_counts)
most_played_index = play_counts.index(max_plays)
print(f"Most played: {playlist[most_played_index]} with {max_plays} plays")
