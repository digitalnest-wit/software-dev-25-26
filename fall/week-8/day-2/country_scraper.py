import requests
import bs4
import sys
import typing
import csv

def fetch_page(url: str) -> requests.Response:
    headers = {
        "User-Agent": "Digital NEST Scraper"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response
    except requests.RequestException as error:
        print(f"Error fetching {url}: {error}")
        sys.exit(1)


def scrape_countries(url: str) -> list[dict]:
    response = fetch_page(url)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    
    country_tags = soup.find_all("div", class_="country")
    country_data = []
    
    for country in country_tags:
        name = country.find("h3", class_="country-name")
        if name is None: continue
        
        capital = country.find("span", class_="country-capital")
        if capital is None: continue
        
        population = country.find("span", class_="country-population")
        if population is None: continue
        
        area = country.find("span", class_="country-area")
        if area is None: continue
        
        country_info = {
            "name": name.text.strip(),
            "capital": capital.text.strip(),
            "population": int(population.text.strip()),
            "area": float(area.text.strip()),
        }
        country_data.append(country_info)
        
    return country_data


def export_to_csv(country_data: list[dict]):
    with open(file="countries.csv", mode="w", encoding="utf-8") as file:
        fieldnames = ["name", "capital", "population", "area"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(country_data)


def filter_countries(file: str, key: typing.Callable[[dict], bool]) -> list[dict]:
    with open(file, mode="r", encoding="utf-8") as f:
        fieldnames = ["name", "capital", "population", "area"] 
        reader = csv.DictReader(f, fieldnames=fieldnames)
        
        # The reason we call next(reader) is so our loop can skip the header.
        #   countries.csv:
        #     1. name,capital,population,area 
        # Recall that the header is the *first* line in the CSV file.. 
        next(reader)
        
        results = []
        
        for row in reader:
            if key(row):
                results.append(row)
    
        return results


def is_big_country(country: dict) -> bool:
    population = int(country["population"])
    return population > 100_000_000

# Testing:
if __name__ == "__main__":
    result = filter_countries(file="countries.csv", key=is_big_country)
    print(result)
