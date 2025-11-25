# Erick

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


def scrape_genres() -> list[str]:
    url = "https://books.toscrape.com/catalogue/page-1.html"
    response = fetch(url)
    soup = bs4.BeautifulSoup(response.content, features='html.parser')
    
    nav_list = soup.find("ul", class_="nav-list")
    if nav_list is None:
        print('couldn\'t find elemnts for \'ul.nav-list\'')
        return []
    
    genre_links = nav_list.find_all('a')
    genres = []
    
    for anchor in genre_links:
        genre_url = anchor.attrs.get("href", None)
        if genre_url is None:
            continue
    
        genre = str(genre_url).removeprefix('category/books/') \
            .removesuffix('/index.html')
        
        genres.append(genre)
    
    # Skip the first entry. It's not a genre, but a link
    # to see *all* the books
    return genres[1:]


def scrape_num_books(genre: str) -> int:
    num_books = 0
    page_num = 1
    page = "index.html"
    
    while True:
        if page_num > 1:
            page = f"page-{page_num}.html"
        
        url = f"https://books.toscrape.com/catalogue/category/books/{genre}/{page}"
        response = fetch(url)
        soup = bs4.BeautifulSoup(response.content, features='html.parser')
        print(f'{genre}: scraping page ({page_num}) for books')
    
        num_books += len(list(soup.find_all("article", class_="product_pod")))
        
        next_btn = soup.find("li", class_="next")
        if next_btn is None:
            return num_books
        
        page_num += 1
        time.sleep(1)


def load_data() -> list[dict[str, typing.Any]]:
    file_name = 'books_per_genre.csv'
    
    if not os.path.exists(file_name):
        genres = scrape_genres()
        num_books_per_genre = list(map(scrape_num_books, genres))
        
        data = [{"genre": g, "num_books": n}
                for g, n in zip(genres, num_books_per_genre)]
        
        export_to_csv(file_name, data)
        print(f"saved data to {os.path.curdir}/{file_name}")
    
    return sorted(import_from_csv(file_name),
                       key=lambda x: int(x["num_books"]),
                       reverse=True)


def format_genre(genre: str) -> str:
    return genre.split('_')[0].title().replace('-', ' ')


def main():
    book_data = load_data()
    genres = [format_genre(b["genre"]) for b in book_data]
    books = [int(b["num_books"]) for b in book_data]
    
    plt.style.use("Solarize_Light2")
    plt.barh(genres[:10], books[:10], color="#D4AB63")
    plt.title("Most Books Per Genre", fontweight='bold')
    plt.xlabel("Book Amount", fontweight='bold')
    plt.ylabel("Genre", fontweight='bold')
    plt.tight_layout()
    plt.grid(axis='x', alpha=0.5, linestyle='--', color="#B8BAA7")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
