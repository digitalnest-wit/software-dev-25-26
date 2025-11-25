# Gabriel

import csv
import os
import sys
import time
import typing

import bs4
import matplotlib.pyplot as plt
import requests

def fetch(url: str) -> requests.Response:
    """Fetch the contents of the page at `url`.

    Args:
        url (str): The URL of the page to fetch.

    Returns:
        requests.Response: The page response object.
    """
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


def export_to_csv(file_name: str, data: list[dict[str, typing.Any]]):
    """Exports data into a CSV file.

    Args:
        file_name (str): The name of the new file to create (should be a CSV file).
        data (list[dict[str, typing.Any]]): The data to export.

    Raises:
        ValueError: When `data` is empty.
    """
    if len(data) == 0:
        raise ValueError("'data' is empty, nothing to write.")
    
    with open(file_name, mode="w", encoding="utf-8") as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        writer.writerows(data)


def import_from_csv(file_name: str) -> list[dict[str, typing.Any]]:
    """Imports CSV data from `file_name`.

    Args:
        file_name (str): The name of the file to import.

    Returns:
        list[dict[str, typing.Any]]: The data loaded from the file.
    """
    with open(file_name, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        # Skip the header
        next(reader)
        
        return [record for record in reader]


def scrape_authors() -> dict[str, typing.Any]:
    authors_quoted = {}
    num_pages = 10
    
    for page in range(1, num_pages + 1):
        response = fetch(f"https://quotes.toscrape.com/page/{page}/")
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        
        author_elements = soup.find_all("small", class_="author")
        for element in author_elements:
            author_name = str(element.text).strip().title()
            
            times_quoted = authors_quoted.get(author_name, 0)
            authors_quoted[author_name] = times_quoted + 1
            
        print(f"scraped page {page} of {num_pages}")
        time.sleep(1 if page < num_pages else 0)
    
    return authors_quoted


def load_data() -> list[dict[str, typing.Any]]:
    file_name = "authors_quoted.csv"
    
    if not os.path.exists(file_name):
        authors_quoted = [
            {
                "author": a,
                "times_quoted": int(n)
            }
            
            for a, n in scrape_authors().items()
        ]
        
        export_to_csv(file_name, authors_quoted)
        print(f"saved data to {file_name}")
    
    return sorted(
        import_from_csv(file_name),
        key=lambda x: x["times_quoted"],
        reverse=True
    )


def main():
    author_data = load_data()    
    author_names = [a["author"] for a in author_data]
    author_count = [int(a["times_quoted"]) for a in author_data]

    plt.style.use("dark_background")
    plt.barh(author_names[:10], author_count[:10])
    plt.title("Top 10 Most Quoted Authors", fontweight='bold')
    plt.xlabel("Times Quoted", fontweight='bold')
    plt.ylabel("Author", fontweight='bold')
    plt.tight_layout()
    plt.grid(axis='x', alpha=0.5, linestyle='--')
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
