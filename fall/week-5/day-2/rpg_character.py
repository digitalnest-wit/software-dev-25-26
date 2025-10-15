# RPG Character Creator

name = input("Enter character name: ")
char_class = input("Enter class (Warrior/Mage/Summoner): ")

# Create character dictionary
character = {
    "name": name,
    "class": char_class,
    "level": 1,
    "health": 100,
    "attack": 10
}

# Display character
print(f"\n{character["name"]} the {character["class"]}")
print(f"Level {character["level"]} - HP: {character["health"]} - ATK: {character["attack"]}")

# Add gold
character["gold"] = 100

# Apply class bonus
if character["class"].lower() == "warrior":
    character["health"] += 20
elif character["class"].lower() == "mage":
    character["attack"] += 5
elif character["class"].lower() == "summoner":
    character["health"] += 10

# Show updated stats
print(f"\nFinal Stats:")
print(f"HP: {character['health']} - ATK: {character['attack']} - Gold: {character['gold']}")
