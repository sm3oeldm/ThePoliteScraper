headers = {
    "User-Agent": "ThePoliteScraper/1.0 (Educational Project; +https://github.com/sm3oeldm/ThePoliteScraper)"
}
ROBOTS_URL = "https://books.toscrape.com/robots.txt"

import requests
import time
def fetchRobot():
    response = requests.get(url = ROBOTS_URL, headers = headers, timeout = 10)

    if response.status_code == 404 or response.status_code == 403:
        return {"detail": "no restrictions"}

    elif response.status_code == 200:
        return response.text

    else:
        return {"detail": f"unexpected status: {response.status_code}"}


def parseRobot(text: str):
    rules = {"crawl_delay": 5, "disallowed": []}

    for line in text.split("\n"):
        line = line.strip()

        if line.startswith("Crawl-delay:"):
            rules["crawl_delay"] = int(line.split(": ")[1])

        elif line.startswith("Disallow"):
            path = line.split(": ")[1]
            if path:
                rules["disallowed"].append(path)

    return rules


def isAllowed(url: str, disallowed_paths: list):
    for path in disallowed_paths:
        if path in url:
            return False

    return True


def rateLimit(delay: int):
    time.sleep(delay)






if __name__ == "__main__":
    text = fetchRobot()
    print("fetchRobot result:", text)
    if isinstance(text, str):
        rules = parseRobot(text)
        print("Parsed rules:", rules)