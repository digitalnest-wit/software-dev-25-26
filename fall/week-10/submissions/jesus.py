# Are Highly Rated Books More Expensive?
import requests
import sys
import bs4
import csv
import pprint
import os
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
    
def scrape_books_data():
    page = "index.html"
    books_data = []
    
    for page_num in range(1, 50 + 1):
        if page_num > 1:
            page = f"page-{page_num}.html"
        
        url = f"https://books.toscrape.com/catalogue/category/books_1/{page}"
        response = fetch_page(url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        print(f"scraping page {page_num} of 50..")
        
        books_rows = soup.find_all("article", class_="product_pod")    

        for row in books_rows:
            rating_tag = row.find("p", class_="star-rating")
            if rating_tag is None: continue
            
            price = row.find("div", class_="product_price")
            if price is None: continue 
            
            price = str(price.find("p").text).strip().removeprefix("£")
            _, rating = rating_tag.attrs["class"]

            if rating == "One":
                rating = 1
            elif rating == "Two":
                rating = 2
            elif rating == "three":
                rating = 3
            elif rating == "four":
                rating = 4
            else:
                rating = 5
                
            book_entry = {
                "price": float(price),
                "rating": rating,
            }
            books_data.append(book_entry)
        
    return books_data
 
def main():
    if not os.path.exists("pricevsrating.csv"):
        books_data =  scrape_books_data()
        export_to_csv("pricevsrating.csv", books_data)
        
    books_data = read_csv(file_name="pricevsrating.csv")
    
    price_groups = {price: [] for price in range(10, 71, 10)} 
    
    for record in books_data: 
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
    price_groups = list(map(lambda p: f"≤ ${p}" , price_groups.keys()))
            
            

    plt.barh(price_groups, average_ratings_within_group, color = 'purple', linewidth=3.0)
    
    # Add labels and title
    plt.xlabel('Book Ratings')
    plt.ylabel('Book Prices')
    plt.title('Are books that are highly rated cost more?')

    # Add a grid to make it easier to read
    plt.grid(True, alpha=0.3)

    # Display the chart
    plt.show()
    

if __name__ == "__main__": 
    main()
