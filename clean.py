RATE = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def cleanBook(data: dict) -> dict:
    data["price"] = float(data["price"][2:])
    data["rating"] = RATE[data["rating"]]

    start = data["Availability"].index("(")
    availability = data["Availability"][start + 1:data["Availability"].index(" ", start)]
    data["Availability"] = int(availability)

    data["Price (excl. tax)"] = float(data["Price (excl. tax)"][2:])
    data["Price (incl. tax)"] = float(data["Price (incl. tax)"][2:])
    data["Tax"] = float(data["Tax"][2:])

    data["Number of reviews"] = int(data["Number of reviews"])

    return data