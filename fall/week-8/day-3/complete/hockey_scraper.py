import requests
import sys
import bs4
import csv
from pprint import pprint

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
    # Return if there is no data to export
    if len(data) == 0:
        print("No data to export!")
        return

    with open(file_name, mode="w", encoding="utf-8") as file:
        # Use the keys of the first data entry for the fieldnames
        fieldnames = data[0].keys()
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def read_csv(file_name: str) -> list[dict]:
    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        # Skip the header
        next(reader)
        
        return [entry for entry in reader]
        # Equivalent to:
        #
        # results = []
        # for entry in reader:
        #     results.append(entry)
        # return results


if __name__ == "__main__":
    url = "https://www.scrapethissite.com/pages/forms/"
    response = fetch_page(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    # Find the table rows
    team_elements = soup.find_all("tr", class_="team")

    # Extract data from each row in the teams table
    team_data = []
    for team in team_elements:
        team_name = team.find("td", class_="name")
        if team_name is None: continue
        team_year = team.find("td", class_="year")
        if team_year is None: continue
        team_losses = team.find("td", class_="losses")
        if team_losses is None: continue
        team_goals = team.find("td", class_="gf")
        if team_goals is None: continue
        
        record = {
            "name": str(team_name.text).strip(),
            "year": int(str(team_year.text).strip()),
            "losses": int(str(team_losses.text).strip()),
            "goals": int(str(team_goals.text).strip()),
        }
        
        # Store in list of dictionaries
        team_data.append(record)
        
    # Export to CSV
    export_to_csv("hockey_stats.csv", data=team_data)
    
    # Read the CSV data
    team_data = read_csv("hockey_stats.csv")
    pprint(team_data)
