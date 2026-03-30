import requests
from bs4 import BeautifulSoup
import json

BASE_URL= 'https://quotes.toscrape.com/'


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def parse_quotes(soup):
    quotes_data = []
    authors_set = set()
    url = BASE_URL
    while url:
        soup = get_soup(url)
        quotes = soup.find_all("div", class_ = 'quote')
        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]

        quotes_data.append({
            "tags": tags,
            "author": author,
            "quote": text
        })
        authors_set.add(author)
        next_btn = soup.find("li", class_="next")
        if next_btn:
            url = BASE_URL + next_btn.find("a")["href"]
        else:
            url = None

    return quotes_data, authors_set


def parse_authors(authors_set):
    authors_data = []

    for author in authors_set:
        url = f"{BASE_URL}/author/{author.replace(' ', '-')}"
        soup = get_soup(url)

        fullname = soup.find("h3", class_="author-title").text.strip()
        born_date = soup.find("span", class_="author-born-date").text.strip()
        born_location = soup.find("span", class_="author-born-location").text.strip()
        description = soup.find("div", class_="author-description").text.strip()

        authors_data.append({
            "fullname": fullname,
            "born_date": born_date,
            "born_location": born_location,
            "description": description
        })

    return authors_data


if __name__ == "__main__":
    quotes, authors_set = parse_quotes(BASE_URL)
    authors = parse_authors(authors_set)

    # Збереження quotes.json
    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)

    # Збереження authors.json
    with open("authors.json", "w", encoding="utf-8") as f:
        json.dump(authors, f, ensure_ascii=False, indent=4)

    print("✅ Дані успішно зібрані!")