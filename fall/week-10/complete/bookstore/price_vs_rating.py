# Jesus

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


def rating_str_to_int(rating: str) -> int:
    match rating.lower():
        case 'one':   return 1
        case 'two':   return 2
        case 'three': return 3
        case 'four':  return 4
        case 'five':  return 5
        case _:       return 0


def scrape_book_data() -> list[dict[str, typing.Any]]:
    next_page = "page-1.html"
    url = f"https://books.toscrape.com/catalogue/category/books_1/{next_page}"
    book_data = []
    
    while True:
        response = fetch(url)
        soup = bs4.BeautifulSoup(response.content, features='html.parser')
        print(f"processing {next_page}..")
        
        book_tags = soup.find_all("article", class_="product_pod")
        for tag in book_tags:
            rating_element = tag.find("p", class_="star-rating")
            if rating_element is None:
                continue
            
            rating_element_classes = rating_element.attrs.get("class", [])
            if len(rating_element_classes) != 2:
                continue
            
            _, rating_str = rating_element_classes
            rating = rating_str_to_int(rating_str)
            
            price_element = tag.find("p", class_="price_color")
            if price_element is None:
                continue
            
            price = str(price_element.text).strip().removeprefix('£')
            price = float(price)
            
            book_data.append({
                "price": price,
                "rating": rating
            })
        
        next_btn = soup.find("li", class_="next")
        if next_btn is None:
            return book_data
        
        next_anchor = next_btn.find("a")
        if next_anchor is None:
            return book_data

        next_page = next_anchor.attrs.get("href", "")
        if next_page == "":
            return book_data
        
        url = f"https://books.toscrape.com/catalogue/category/books_1/{next_page}"


def load_data() -> list[dict[str, typing.Any]]:
    filename = "price_vs_rating.csv"
    
    if not os.path.exists(filename):
        book_data = scrape_book_data()
        export_to_csv(filename, book_data)
    else:
        book_data = import_from_csv(filename)
    
    return book_data


def plot(book_data: list[dict[str, typing.Any]]):    
    price_groups = {price: [] for price in range(10, 71, 10)}
    
    for record in book_data:
        price = float(record.get("price", 0))
        rating = int(record.get("rating", 0))
        
        if 0 <= price < 10.5:
            price_groups[10].append(rating)
        elif 10.5 <= price < 20.5:
            price_groups[20].append(rating)
        elif 20.5 <= price < 30.5:
            price_groups[30].append(rating)
        elif 30.5 <= price < 40.5:
            price_groups[40].append(rating)
        elif 40.5 <= price < 50.5:
            price_groups[50].append(rating)
        elif 50.5 <= price < 60.5:
            price_groups[60].append(rating)
        else:
            price_groups[70].append(rating)       
    
    price_groups = {
        group: sum(r) / len(r)
        for group, r in price_groups.items()
        if len(r) != 0
    }
    average_ratings_within_group = list(price_groups.values())
    price_groups = list(map(lambda p: f"${p}+", price_groups.keys()))
    
    plt.style.use("dark_background")
    
    plt.barh(price_groups, average_ratings_within_group, color="#e82ea7")
    plt.title("Are Expensive Books Better Rated?", fontweight='bold')
    plt.xlabel("Rating", fontweight='bold')
    plt.ylabel("Prices", fontweight='bold')

    plt.grid(axis='x', alpha=0.5, linestyle='--', color="#e3f9af")
    
    plt.show()
    

def main():
    n = 1000
    book_data = load_data()
    
    plot(book_data)
    # plot_scatter(book_data)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
