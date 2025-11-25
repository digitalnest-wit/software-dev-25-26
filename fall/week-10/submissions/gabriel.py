# Top 10 Most Quoted Authors
import requests
import sys
import bs4
import csv
import pprint
import time
import matplotlib.pyplot as plt
import os


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
    
def scrape_author_data():
    n = 1
    num_pages = 10

    authors = {}
    while n <= num_pages:
        url = f"https://quotes.toscrape.com/page/{n}/"
        response = fetch_page(url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        print(f"scraping page {n}/{num_pages}..")

        author_elements = soup.find_all("small", class_="author")

        for author in author_elements:
            author = str(author.text).strip()
            authors[author] = authors.get(author,0) + 1

        n += 1 
        time.sleep(1)

    return [
        {
            "author": a,
            "num_quotes": int(n)
        }
        for a, n in authors.items()
    ]

def load_data():
    filename = "top_quoted.csv"
    if not os.path.exists(filename):
        data = scrape_author_data()
        export_to_csv(filename, data)

    return read_csv(filename)    
        

if __name__ == "__main__":
    data = sorted(load_data(), key=lambda x: x["num_quotes"], reverse=True)
    authors = [x["author"] for x in data][:10]
    num_quotes = [int(x["num_quotes"]) for x in data][:10]

    plt.barh(authors, num_quotes ,color = "#a39b90")

    # Add labels and title
    plt.xlabel('# Of Quotes')
    plt.ylabel('Author Name')
    plt.title('Top 10 Most Quoted Authors')

    # Make the layout fit better
    plt.tight_layout()

    # Display the chart
    plt.show()