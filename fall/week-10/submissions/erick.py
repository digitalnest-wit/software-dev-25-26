# Number of Books per Genre

import requests
import bs4
import sys
import typing
import pprint
import csv
import matplotlib.pyplot as plt

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
    if len(data) == 0:
        print("No data to export!")
        return

    with open(file_name, mode="w", encoding="utf-8") as file:
        fieldnames = data[0].keys()
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def read_csv(file_name: str) -> list[dict]:
    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        next(reader)
        
        return [entry for entry in reader]

def scrape_genres():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    respone = fetch_page(url)
    soup = bs4.BeautifulSoup(respone.content, "html.parser")

    navlist = soup.find('ul', class_='nav')
    if navlist is None:
        return []
    
    genre_links = navlist.find_all("a")

    genres = []

    for i, genre in enumerate(genre_links, start=1):
        genre = str(genre.text).strip()
        genre = genre.lower().replace(" ", "-")
        genre = f"{genre}_{i}"

        genres.append(genre)
    
    return genres[1:]

def scrape_num_books(genre: str) -> int:

    page_num = 1

    num_books = 0

    while True:
        page = "index.html" if page_num == 1 else f"page-{page_num}.html"
        url = f"https://books.toscrape.com/catalogue/category/books/{genre}/{page}"
        response = fetch_page(url)
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        print(f"scraping {genre}.found {page_num}")

        num_books += len(list(soup.find_all("article", class_="product_pod")))

        next_bth = soup.find("li", class_="next")

        if next_bth is None:
            return num_books
        
        page_num += 1


def main():
    genres = scrape_genres()
    num_books_per_genre = {}

    for genre in genres:
        num = scrape_num_books(genre)
        num_books_per_genre[genre] = num

    plt.bar(genres, list(num_books_per_genre.values()))

    plt.xlabel('Genres')
    plt.ylabel('Number of Books')
    plt.title('Nuber of Books per Genre')

    plt.xticks(rotation=45, ha='right')


    plt.tight_layout()


    plt.show()

if __name__ == "__main__":
    main()

