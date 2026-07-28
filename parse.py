from bs4 import BeautifulSoup

def parseListPage(html: str):
    cc = BeautifulSoup(html, "html.parser")
    bookCards = cc.find_all("article", class_="product_pod")

    extracted = []
    for item in bookCards:
        extracted.append({
            "title": item.find("h3").find("a")["title"],
            "price": item.find("p", class_ = "price_color").text,
            "rating": item.find("p", class_ = "star-rating")["class"][1],
            "url": item.find("h3").find("a")["href"]
        })

    return extracted


if __name__ == "__main__":
    from fetch import fetchPage
    html = fetchPage("https://books.toscrape.com/catalogue/page-1.html")
    books = parseListPage(html)
    print(f"Found {len(books)} books")
    for b in books[:3]:
        print(b)