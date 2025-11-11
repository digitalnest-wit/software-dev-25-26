import matplotlib.pyplot as plt
import csv

teams = []
wins = []

with open('hockey_stats.csv', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        teams.append(row['name'])
        wins.append(int(row['wins']))

# Combine the team names and wins
teams_data = list(zip(teams, wins))
# Sort the data by wins (most to least)
winning_teams = sorted(teams_data, key=lambda team: team[1], reverse=True)

# Pick the first five items in the list
top_5_winning_teams = winning_teams[:5]
# Extract the team names
top_5_teams = [team[0] for team in top_5_winning_teams]
# Extract the team wins
top_5_wins = [team[1] for team in top_5_winning_teams]

# Create a horizontal bar chart using the team names and wins
plt.barh(top_5_teams, top_5_wins)

# Add labels and title
plt.xlabel('Wins')
plt.ylabel('Teams')
plt.title('Top 5 Teams by Wins')

# Make the layout fit better
plt.tight_layout()

# Display the chart
plt.show()
