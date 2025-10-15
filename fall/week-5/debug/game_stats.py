# Game Stats Tracker (BUGGY VERSION)

print("=== Game Stats Tracker ===\n")

# Player stats dictionary
player_stats = {
    "username": "Player1",
    "level": 5,
    "wins": 12,
    "losses": 8,
    "kills": 45,
    "deaths": 32
}

# Display current stats
print(f"Player: {player_stats['username']}")
print(f"Level: {player_stats['level']}")
print(f"Record: {player_stats['wins']}-{player_stats['losses']}")
print(f"K/D: {player_stats['kills']}/{player_stats['deaths']}")

# Bug 1: KeyError - trying to access a key that doesn't exist
print(f"Score: {player_stats['score']}")

# Bug 2: Missing assignment operator
print("\n=== Game Results ===")
result = input("Did you win? (yes/no): ")

if result == "yes":
    player_stats["wins"] = player_stats["wins"] + 1
    player_stats["level"] + 1 
else:
    player_stats["losses"] += 1

# Bug 3: Trying to add new stat with wrong syntax
player_stats("matches_played") = 20

# Update kills and deaths
new_kills = int(input("Kills this game: "))
new_deaths = int(input("Deaths this game: "))

player_stats["kills"] += new_kills
player_stats["deaths"] += new_deaths

# Bug 4: Using wrong method - trying to get a key that might not exist
experience = player_stats["experience"]  # Should use .get() with default value

# Calculate win rate
total_games = player_stats["wins"] + player_stats["losses"]
win_rate = player_stats["wins"] / total_games * 100

# Display updated stats
print("\n=== Updated Stats ===")
print(f"Player: {player_stats['username']}")
print(f"Level: {player_stats['level']}")
print(f"Record: {player_stats['wins']}-{player_stats['losses']}")
print(f"Win Rate: {win_rate}%")
print(f"K/D Ratio: {player_stats['kills'] / player_stats['deaths']}")
print(f"Total Matches: {player_stats['matches_played']}")
print(f"Experience: {experience}")