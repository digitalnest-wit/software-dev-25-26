import matplotlib.pyplot as plt
import csv

# The data we're interested in collecting
teams = []
wins = []

with open('hockey_stats.csv', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # TODO: append the data into the lists
        #   hint: what data are we interested in?
        #   hint: what method do we use to append data to a list?
        pass

# Combine the team names and wins
teams_data = list(zip(teams, wins))
# Sort the data by wins (most to least)
winning_teams = sorted(teams_data, key=lambda team: team[1], reverse=True)

# TODO: Pick the first five items in the list
top_5_winning_teams = winning_teams[:]

# Extract the team names
top_5_teams = [team[0] for team in top_5_winning_teams]
# Extract the team wins
top_5_wins = [team[1] for team in top_5_winning_teams]

# TODO: Create a horizontal bar chart using the team names and wins

# TODO: Add labels and title

# Make the layout fit better
plt.tight_layout()

# TODO: Display the chart
