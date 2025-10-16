print("=== Game Stats Tracker ===\n")

player_stats = {
    "username": "Player1",
    "level": 5,
    "wins": 12,
    "losses": 8,
    "kills": 45,
    "deaths": 32
}

# Display current stats
print(f"Player:       {player_stats['username']}")
print(f"Level:        {player_stats['level']}")
print(f"Wins:         {player_stats['wins']}")
print(f"Losses:       {player_stats['losses']}")
print(f"Kills/Deaths: {player_stats['kills']}/{player_stats['deaths']}")

# Display the 'score' stat (hint: may not exist. check if the key exists first)
print(f"Score: {player_stats['score']}")

print("\n=== Game Results ===")
result = input("Did you win? (yes/no): ")

# Update player stats depending on whether they won or not
if result == "yes":
    player_stats["wins"] = player_stats["wins"] + 1
    player_stats["level"] + 1 
else:
    player_stats["losses"] += 1

# Add new stat, 'matches_played'
player_stats("matches_played") = 20

# Update kills and deaths
new_kills = int(input("\nHow many kills this last game?: "))
new_deaths = int(input("How many deaths this last game?: "))

player_stats["kills"] += new_kills
player_stats["deaths"] += new_deaths

# Get the 'experience' stat value. (hint: might not exist. which dict method
# gets you a value and provides a way to return a default value if the key
# doesn't exist?)
experience = player_stats["experience"]

# Calculate win rate
total_games = player_stats["wins"] + player_stats["losses"]
win_rate = player_stats["wins"] / total_games * 100

# Display updated stats
print("\n=== Updated Stats ===")
print(f"Player:        {player_stats['username']}")
print(f"Level:         {player_stats['level']}")
print(f"Record:        {player_stats['wins']}-{player_stats['losses']}")
print(f"Win Rate:      {win_rate}%")
print(f"K/D Ratio:     {player_stats['kills'] / player_stats['deaths']}")
print(f"Total Matches: {player_stats['matches_played']}")
print(f"Experience:    {experience}")
