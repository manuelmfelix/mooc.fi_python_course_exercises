# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def order_by_rating(item: dict):
        return item['rating']
        
    return sorted(items, key=order_by_rating, reverse=True)


if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")