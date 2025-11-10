import requests
import bs4
import sys
import typing


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
    
    country_tags = soup.select("#page div.row:nth-child(n + 4) .country")
    print(f"Found {len(country_tags)} tags")

    return []

# Testing:
if __name__ == "__main__":
    url = "https://www.scrapethissite.com/pages/simple/"
    scrape_countries(url)
