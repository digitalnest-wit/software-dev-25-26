# Cristobal

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
    
    # Find all links within the 'nav-list', scraping the text for
    # each link
    genre_links = nav_list.find_all('a')
    genres = [
        # Format the genre to appear exactly as it does within a URL,
        # with the form '<genre-name>_<offset>'
        str(anchor.text).strip().lower().replace(" ", "-") + f"_{i}"
        for i, anchor in enumerate(genre_links, start=1)
    ]
    
    # Skip the first entry. It's not a genre, but a link
    # to see *all* the books
    return genres[1:]


def rating_str_to_int(rating: str) -> int:
    match rating.lower():
        case 'one':   return 1
        case 'two':   return 2
        case 'three': return 3
        case 'four':  return 4
        case 'five':  return 5
        case _:       return 0


def scrape_avg_ratings(genre: str) -> float:
    page_num = 1
    page = "index.html"
    
    while True:
        if page_num > 1:
            page = f"page-{page_num}.html"
        
        url = f"https://books.toscrape.com/catalogue/category/books/{genre}/{page}"
        response = fetch(url)
        soup = bs4.BeautifulSoup(response.content, features='html.parser')
        
        ratings = []
        book_tags = soup.find_all("article", class_="product_pod")
        print(f"{genre:<25} scraping page.. {page_num}")
        
        for tag in book_tags:
            # Scrape the element that contains the 'star-rating' class.
            rating_element = tag.find("p", class_="star-rating")
            if rating_element is None:
                continue
            
            # Get the class list attribute from the element
            rating_element_classes = rating_element.attrs.get("class", [])
            if len(rating_element_classes) != 2:
                continue
            
            # Extract the rating class ('One', 'Two', etc.) and map it to
            # its integer value.
            _, rating_str = rating_element_classes
            rating = rating_str_to_int(rating_str)
            ratings.append(rating)
        
        # Stop and return when there is no 'next' page button.
        next_btn = soup.find("li", class_="next")
        if next_btn is None:
            print(f"{genre:<25} done. found {page_num} {'page' if page_num == 1 else 'pages'}")
            return sum(ratings) / len(ratings)
        
        page_num += 1
        time.sleep(1)


def format_genre(genre: str) -> str:
    return genre.split('_')[0].title().replace('-', ' ')

def load_data() -> list[dict[str, typing.Any]]:
    filename = "avg_ratings_per_genre.csv"
    
    if not os.path.exists(filename):
        ratings_per_genre = [
            {
                "genre": format_genre(g),
                "avg_rating": float(scrape_avg_ratings(g))
            }

            for g in scrape_genres()
        ]
        
        export_to_csv(filename, ratings_per_genre)
    
    return import_from_csv(filename)


def plot(genres: list[str], ratings: list[float], ):
    
    def det_bar_color(width: float) -> str:
        if 0 <= width < 2:
            return "#e25c5c"
        elif 2 <= width < 3.5:
            return "#e2aa5c"
        elif 3.5 <= width < 4.5:
            return "#eee260"
        else:
            return "#89dc51"
    
    plt.style.use("Solarize_Light2")
    bar_colors = [det_bar_color(x) for x in ratings]
    plt.barh(genres, list(map(lambda x: x, ratings)), color=bar_colors, height=0.95)
    
    plt.title("Average Book Ratings Per Genre", fontweight='bold')
    plt.xlabel("Ratings", fontweight='bold')
    plt.ylabel("Genres", fontweight='bold')
    plt.tight_layout()
    plt.grid(axis='x', alpha=0.5, linestyle='--', color="#B8BAA7")
    
    plt.show()


def main():
    n = 15
    ratings_per_genre = load_data()
    
    highest_rated = sorted(
        ratings_per_genre,
        key=lambda x: float(x["avg_rating"]),
        reverse=True
    )
    genres = [x["genre"] for x in highest_rated][:n][::-1]
    ratings = [float(x["avg_rating"]) for x in highest_rated][:n][::-1]
    
    plot(genres, ratings)
    
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
