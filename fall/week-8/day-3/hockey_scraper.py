# Create a program that scrapes the hockey statistics table on this site:
#   https://www.scrapethissite.com/pages/forms/
# Your program should extract
#   - the team name
#   - year
#   - wins
#   - losses
#   - goals for each team
#
# Stores extracted data in a list of dictionaries, then
# Exports to a CSV file named hockey_stats.csv.
#
# BONUS: Filter to show only teams with winning records (wins > losses)

import requests
import sys
import bs4
import csv
import pprint

def fetch_page(url: str) -> requests.Response:
    headers = {
        "User-Agent": "Digital NEST Scraper (leo@digitalnest.org)"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response
    except requests.RequestException as error:
        print(f"Error fetching {url}: {error}")
        sys.exit(1)

def export_to_csv(file_name: str, data: list[dict]):
    # Returns if there is no data to export
    if len(data) == 0:
        print("No data to export!")
        return

    with open(file_name, mode="w", encoding="utf-8") as file:
        # Uses the keys of the first data entry for the fieldnames
        fieldnames = data[0].keys()
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def read_csv(file_name: str) -> list[dict]:
    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        # Skips the header
        next(reader)
        
        return [entry for entry in reader]
        # Equivalent to:
        #
        # results = []
        # for entry in reader:
        #     results.append(entry)
        # return results

def scrape_hockey_data():
    url = "https://www.scrapethissite.com/pages/forms/"
    response = fetch_page(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    # Find the table rows for each team
    team_rows = soup.find_all("tr", class_="team")
    
    # TODO: Extract data from each row
    #   - the team name
    #   - year
    #   - wins
    #   - losses
    #   - goals for each team
    
    teams_data = []
    
    for row in team_rows:
        name = row.find("td", class_="name")
        if name is None: continue
        name = str(name.text).strip()
        
        year = row.find("td", class_="year")
        if year is None: continue
        year = int(str(year.text).strip())
        
        wins = row.find("td", class_="wins")
        if wins is None: continue
        wins = int(str(wins.text).strip())
        
        losses = row.find("td", class_="losses")
        if losses is None: continue
        losses = int(str(losses.text).strip())

        goals = row.find("td", class_="gf")
        if goals is None: continue
        goals = int(str(goals.text).strip())
        
        team_data = {
            "name": name,
            "year": year,
            "wins": wins,
            "losses": losses,
            "goals": goals,
        }
        teams_data.append(team_data)

    # Export to a CSV file named hockey_stats.csv.
    export_to_csv(file_name="hockey_stats.csv", data=teams_data)


if __name__ == "__main__":
    teams_data = read_csv(file_name="hockey_stats.csv")
    
    for team in teams_data:
        team["year"]   = int(team["year"])
        team["wins"]   = int(team["wins"])
        team["losses"] = int(team["losses"])
        team["goals"]  = int(team["goals"])
    
    results = list(filter(lambda team: team["goals"] > 300, teams_data))
    pprint.pprint(results)
    