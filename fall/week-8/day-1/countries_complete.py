import requests
import sys
import bs4
import typing

def fetch_page(url: str) -> requests.Response:
    """Fetch webpage with proper headers and error handling."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Educational Purpose)'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        sys.exit(1)

def extract_text(tag: bs4.Tag, selector: str, convert_fn: typing.Callable = str):
    """Extract and convert text from a tag. Returns None if not found."""
    element = tag.select_one(selector)
    if element is None:
        return None
    
    text = element.text.strip()
    try:
        return convert_fn(text)
    except (ValueError, TypeError):
        return None

def parse_country(tag: bs4.Tag) -> dict | None:
    """Parse a single country tag into a dictionary."""
    name = extract_text(tag, "h3.country-name")
    if name is None:
        return None
    
    capital = extract_text(tag, "span.country-capital")
    population = extract_text(tag, "span.country-population", int)
    area = extract_text(tag, "span.country-area", float)
    
    return {
        "name": name,
        "capital": capital,
        "population": population,
        "area": area,
    }

def scrape_countries(url: str) -> list[dict]:
    """Main scraping function."""
    response = fetch_page(url)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    
    country_tags = soup.select("#page .row:nth-child(n+4) .country")
    countries = []
    
    for tag in country_tags:
        country = parse_country(tag)
        if country is not None:
            countries.append(country)
    
    return countries

if __name__ == "__main__":
    url = "https://www.scrapethissite.com/pages/simple/"
    countries = scrape_countries(url)
    
    print(f"Scraped {len(countries)} countries\n")
    for country in countries[:5]:
        print(f"  {country['name']}")
        print(f"    Capital:      {country['capital']}")
        print(f"    Population:   {country['population']:,}")
        print(f"    Area (km²):   {country['area']:,}")
        print()
