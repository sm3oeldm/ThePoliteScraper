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


def parseDetailPage(html: str):
    cc = BeautifulSoup(html, "html.parser")
    table = cc.find("table", class_ = "table table-striped")
    tds = table.find_all("td")

    desc_tag = cc.find("div", id="product_description")
    description = desc_tag.find_next_sibling("p").text if desc_tag else ""

    return {
        "UPC": tds[0].text,
        "Product Type": tds[1].text,
        "Price (excl. tax)": tds[2].text,
        "Price (incl. tax)": tds[3].text,
        "Tax": tds[4].text,
        "Availability": tds[5].text,
        "Number of reviews": tds[6].text,
        "Description": description,
    }