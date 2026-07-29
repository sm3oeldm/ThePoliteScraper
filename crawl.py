from fetch import fetchPage
from parse import parseListPage, parseDetailPage
from robots import rateLimit
from clean import cleanBook
from robots import fetchRobot, parseRobot
from bs4 import BeautifulSoup
import re
import csv

URL = "https://books.toscrape.com/catalogue/category/books_1/index.html"

def crawl_category(start_url: str):
    current_url = start_url
    all_books = []

    while current_url:
        html = fetchPage(current_url)
        books = parseListPage(html)

        for book in books:
            clean_url = re.sub(r'^(\.\./)+', '', book["url"])
            detail_url = "https://books.toscrape.com/catalogue/" + clean_url
            try:
                detail_data = parseDetailPage(fetchPage(detail_url))
                rateLimit(1)
                all_books.append(cleanBook({**book, **detail_data}))
            except Exception:
                print(f"Skipped {book['title']} — timed out")

        # Check for next page
        soup = BeautifulSoup(html, "html.parser")
        next_btn = soup.find("li", class_="next")
        if next_btn and next_btn.find("a"):
            next_href = next_btn.find("a")["href"]
            # Construct the next URL relative to the current page
            current_url = current_url.rsplit("/", 1)[0] + "/" + next_href
        else:
            current_url = None

        rateLimit(3)

    return all_books


if __name__ == "__main__":
    books = crawl_category(URL)
    print(f"Category done: {len(books)} books")

    fieldnames = [
        "title", "price", "rating", "url", "UPC", "Product Type",
        "Price (excl. tax)", "Price (incl. tax)", "Tax",
        "Availability", "Number of reviews", "Description"
    ]

    with open("books.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

    print(f"Saved {len(books)} books to books.csv")