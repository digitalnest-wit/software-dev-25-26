# Top 10 Genres by Weighted Average

import matplotlib.pyplot as plt
import csv
import requests
import sys
import bs4
import pprint
from pathlib import Path

plt.style.use('ggplot')

book_genres = []

def color_list(ratings):
    color_list = []
    for rating in ratings:
        if rating >= 3.5:
            color_list.append('green')
        elif rating >= 3.25:
            color_list.append('yellow')
        else:
            color_list.append('red')
    return color_list

def fetch_page(url: str) -> requests.Response:
    headers = {
        "User-Agent": "Digital NEST Scraper (cristobalelizarraraz905@gmail.com)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        print(f"Successfully fetched {url}")
        return response
    except requests.RequestException as error:
        print(f"Error fetching {url}: {error}")
        return 0

def scrape_genres(url: str) -> list[str]:
    response = fetch_page(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    genre_tags = soup.select(".nav-list a")
    genres = [tag.text.strip().lower().replace(" ","-") for tag in genre_tags]
    return genres


def scrape_books(url: str, genre: str) -> list[dict]:
    response = fetch_page(url)
    if(response == 0):
        return []
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    book_tags = soup.select("article.product_pod")
    books = []
    for tag in book_tags:
        rating = tag.select_one("p.star-rating")["class"][1]
        cases = {
            "One": 1.0,
            "Two": 2.0,
            "Three": 3.0,
            "Four": 4.0,
            "Five": 5.0
        }
        rating = cases.get(rating, 0)
        book = {
            "genre" : genre,
            "rating": rating,
        }
        books.append(book)
    return books

def export_to_csv(file_name: str, data: list[dict]):
    if len(data) == 0:
        print("No data to export!")
        return


    file_exists = Path(file_name).exists()
    with open(file_name, mode="a", encoding="utf-8") as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)

def read_csv(file_name: str) -> list[dict]:
    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [entry for entry in reader]

def sorted_ratings(file_name: str,weighted_values: bool, m: float=5.0):
    data = read_csv(file_name)

    all_ratings = [float(entry["rating"]) for entry in data]
    C = sum(all_ratings) / len(all_ratings)

    genre_ratings = {}
    for entry in data:
        genre = entry["genre"]
        rating = float(entry["rating"])
        if genre not in genre_ratings:
            genre_ratings[genre] = []
        genre_ratings[genre].append(rating)

    avg_ratings = {genre: sum(ratings)/len(ratings) for genre, ratings in genre_ratings.items()}
    counts = {g: len(rlist) for g, rlist in genre_ratings.items()}

    # Bayesian weighted score
    weighted = []
    for g in avg_ratings:
        v = counts[g]
        r = avg_ratings[g]
        weighted_score = (v / (v + m)) * r + (m / (v + m)) * C
        weighted.append((g, weighted_score, r, v))

    if(weighted_values==True):
        sorted_genres = sorted(weighted, key=lambda x: x[1], reverse=True)
    else:
        sorted_genres = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)
    return sorted_genres

def scrape_and_export(url: str, file_name: str):
    book_genres = scrape_genres(url)
    # Iterate clearly and safely: enumerate the slice starting at index 2(first isn't a genre)
    for it, genre in enumerate(book_genres[1:], start=2):
        page_iterator = 2
        genre_page_url = f"https://books.toscrape.com/catalogue/category/books/{genre}_{it}/index.html"
        book_data = scrape_books(genre_page_url,genre)
        export_to_csv(file_name, book_data,)
        while True:
            genre_page_url= f"https://books.toscrape.com/catalogue/category/books/{genre}_{it}/page-{page_iterator}.html"
            book_data = scrape_books(genre_page_url, genre)
            if len(book_data) == 0:
                break
            else:
                export_to_csv(file_name, book_data)
                page_iterator += 1

def plot_genre_ratings(file_name: str, weighted_values: bool):
    sorted_data = sorted_ratings(file_name, weighted_values)
    # Pick the Top 10 genres with the highest average ratings
    sorted_data = sorted_data[:10]
    # Extract the genres
    genres = [team[0] for team in sorted_data]
    genres = [genre.replace("-", " ").title() for genre in genres]
    # Extract the ratings
    ratings = [team[1] for team in sorted_data]

    graph = plt.bar(genres, ratings, color=color_list(ratings))
    for bar in graph:
        height = bar.get_height()
        plt.annotate(f'{height:.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", 
                    ha='center', 
                    va='bottom',
                    fontsize=8
                    )
        
    plt.ylabel('Rating')
    plt.xlabel('Genre')
    plt.title('Top 10 Genres by Weighted Average Rating')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    url = "https://books.toscrape.com/index.html"
    file_name = "books_data.csv"
    if not Path(file_name).exists():
        scrape_and_export(url, file_name)
    plot_genre_ratings(file_name, weighted_values=True)
    plot_genre_ratings(file_name, weighted_values=False)
            

