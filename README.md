# ThePoliteScraper

A polite web scraper for [books.toscrape.com](https://books.toscrape.com) — a demonstration site for scraping practice. Built as the data-c
ollection pipeline for a RAG corpus project.

## Pipeline

```
fetch → parse → extract → clean → structure → save
```

| Step | Module | What it does |
|------|--------|-------------|
| **Fetch** | [`fetch.py`](fetch.py) | Downloads HTML with a polite User-Agent and 10s timeout |
| **Parse** | [`parse.py`](parse.py) | (Extracts list-png, URL) and detail-page data (UPC, taxes, description,
etc.) |
| **Clean** | [`clean.py`](clean.py) | (Normalizes raw ring → float/int) |
| **Crawl** | [`crawl.py`](crawl.py) | Orchestrates the full pipeline, handles pagination, rate-limiting, and CSV export |
| **Robots** | [`robots.py`](robots.py) | Robots.txt p and shared `rateLimit()` helper |

## Results

**999 books** scraped (1 skipped due to a transient ti)(books.csv).

Each row contains:

| Field | Type | Example |
|-------|------|---------|
| `title` | string | A Light in the Attic |
| `price` | float | 51.77 |
| `rating` | int (1–5) | 3 |
| `url` | string | `../../a-light-in-the-attic_1000/index.html` |
| `UPC` | string | a897fe39b1053632 |
| `Product Type` | string | Books |
| `Price (excl. tax)` | float | 51.77 |
| `Price (incl. tax)` | float | 51.77 |
| `Tax` | float | 0.0 |
| `Availability` | int | 22 |
| `Number of reviews` | int | 0 |
| `Description` | string | It's hard to imagine a world without... |

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run the scraper
python crawl.py
```

The scraper:

1. Starts at the first category page
2. Fetches each list page and extracts book links
3. Visits every book detail page with a polite delay (2s)
4. Cleans and normalizes all fields
5. Moves to the next page via the "next" button
6. Delays 3s between category pages
7. Saves everything to `books.csv`

## Polite Scraping

- **Custom User-Agent** that identifies the project and provides contact info
- **Per-book rate limit** (2s between detail pages)
- **Per-page rate limit** (3s between list pages)
- **Timeout tolerance** (skips individual books that t)
- **Robots.txt parser** ready for use (not enforced by default)

## Dependencies

- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifuls)

## License

Educational project — built for learning purposes.