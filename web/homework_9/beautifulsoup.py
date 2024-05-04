import json
import re
import os
import requests
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

URL = 'https://quotes.toscrape.com/'


def get_quotes(soup: BeautifulSoup) -> list:
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    quotes_list = []
    for i in range(0, len(quotes)):
        quotes_list.append({
            'tags': [tag.text for tag in tags[i].find_all('a', class_='tag')],
            'author': authors[i].text,
            'quote': quotes[i].text[1:-1]
        })
    return quotes_list


def get_author(soup: BeautifulSoup) -> dict:
    author = soup.find('h3', class_='author-title')
    born = soup.find('span', class_='author-born-date').text
    location = soup.find('span', class_='author-born-location').text
    description = soup.find('div', class_='author-description').text
    return {
        'fullname': author.text,
        'born_date': born,
        'born_location': location,
        'description': re.sub(r'\n', '', description.strip())
    }


def get_authors(soup: BeautifulSoup, processed_authors: list = []) -> list:
    quotes = soup.find_all('div', class_='quote')
    authors_list = []
    for i in range(0, len(quotes)):
        a_tag = quotes[i].find('a')
        relative_url = a_tag['href'] if a_tag else None
        if not relative_url or relative_url in processed_authors:
            continue
        processed_authors.append(relative_url)
        soupAuthor = fetch_page(urljoin(URL, relative_url))
        author = get_author(soupAuthor)
        authors_list.append(author)

    return authors_list, processed_authors


def write_json(file_path, objects: list):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(objects, file, indent=4, ensure_ascii=False)


def fetch_page(url):
    print(f'Fetching page: {url}')
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('Failed to load page')
    return BeautifulSoup(response.text, 'lxml')


def parse():
    soup = fetch_page(URL)
    processed_authors = []
    quotes = []
    authors = []

    while True:
        quotes.extend(get_quotes(soup))
        _authors, processed_authors = get_authors(soup, processed_authors)
        authors.extend(_authors)

        next_page = soup.find('li', class_='next')
        if not next_page:
            break

        soup = fetch_page(urljoin(URL, next_page.find('a')['href']))

    return quotes, authors


if __name__ == '__main__':
    quotes, authors = parse()
    write_json(os.getenv("QUOTES_PATH"), quotes)
    write_json(os.getenv("AUTHORS_PATH"), authors)
