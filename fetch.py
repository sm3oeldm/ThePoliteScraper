# fetch.py is a helper that goes to a webpage and downloads its HTML. Think of it like: you give it a URL, it does HTTP request
# politely, and hands you back the raw page text.

import requests
import time


headers = {
    "User-Agent": "ThePoliteScraper/1.0 (Educational Project; +https://github.com/sm3oeldm/ThePoliteScraper)"
}
booksURL = "https://books.toscrape.com/" 

def fetchPage(url: str):
    response = requests.get(url, headers = headers, timeout = 10)
    response.raise_for_status()

    return response.text
