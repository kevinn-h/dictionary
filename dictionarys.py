kevins_store = [
    {
        "name": "Iphone Duo",
        "price": 1699.99,
        "department": "electronics",
        "description": "very expensive, likely a scam, do not reccomend, but please buy cuz im broke."


    },
    {

        "name": "banana peel",
        "price": 20.00,
        "department": "trash",
        "description": "use it for mario kart but use it WISELY."
    },
    {

    "name": "GTA VI"
    ,"price": 100.00,
    "department": "Video Games",
    "description": "november 19th november 19th november 19th."
    },
    {
    "name": "Mclaren Artura"
    ,"price": 316850.00,
    "department": "Vehicles",
    "description": "Very very fast car🔥"
    },
    {
    "name": "aidens house"
    ,"price": 586850.00,
    "department": "Houses",
    "description": "bro its aidens house buy now or ELSE."
    }
]


def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])

def choose_item():
    show_items(kevins_store)
    x = int(input("Which item number do you want to buy? "))
    print(kevins_store[x])

choose_item()