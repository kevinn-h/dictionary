""" vac = {
    "name": "Dyson V15 Cordless Vacuum",
    "price": 699.99,
    "department": "Appliances",
    "description": "High-powered cordless vacuum with laser dust detection."
}

print(vac["name"])
print(vac["price"]) """

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

shopping_cart = []
total = 0
while True:
    show_items(kevins_store)
    print(" ")
    y = input("Choose an item number, type 'shopping cart', 'checkout', or 'quit': ")
    if y == "shopping cart":
        print("Your shopping cart")
        if shopping_cart:
            for item in shopping_cart:
                print(item["name"], item["price"])
                print(" ")
            Y = input("would you like to checkout?")
        else:
            print("Your cart is empty.")
    
    elif y == "quit":
        print("Goodbye!")
        break
    elif y == "checkout":
        print("receipt")
        for item in shopping_cart:
            print(item["name"], item["price"])
        print("your total is", float(total))
        
        break
    elif y == "0":
        print(kevins_store[0]["name"])
        print(kevins_store[0]["price"])
        print(kevins_store[0]["department"])
        print(kevins_store[0]["description"])
        print(" ")
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            print(" ")
            shopping_cart.append(kevins_store[0])
            print(f"{kevins_store[0]['name']} added to your cart.")
            total +=1055.99
            print(" ")
            Y = input("would you like to check out?")
        else:
            print("Item not added to cart.")
    elif y == "1":
        print(kevins_store[1]["name"])
        print(kevins_store[1]["price"])
        print(kevins_store[1]["department"])
        print(kevins_store[1]["description"])
        print(" ")
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            print(" ")
            shopping_cart.append(kevins_store[1])
            print(f"{kevins_store[1]['name']} added to your cart.")
            total += 200.50
            print(" ")
            Y = input("would you like to check out?")
        else:
            print(" ")
            print("Item not added to cart.")
    elif y == "2":
        print(kevins_store[2]["name"])
        print(kevins_store[2]["price"])
        print(kevins_store[2]["department"])
        print(kevins_store[2]["description"])
        print(" ")
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            print(" ")
            shopping_cart.append(kevins_store[2])
            print(f"{kevins_store[2]['name']} added to your cart.")
            total += 100
            print(" ")
            Y = input("would you like to check out?")
        else:
            print("Item not added to cart.")
    elif y == "3":
        print(kevins_store[3]["name"])
        print(kevins_store[3]["price"])
        print(kevins_store[3]["department"])
        print(kevins_store[3]["description"])
        print(" ")
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            print(" ")
            shopping_cart.append(kevins_store[3])
            print(f"{kevins_store[3]['name']} added to your cart.")
            total += 316850.00
            print(" ")
            Y = input("would you like to check out?")
        else:
            print("Item not added to cart.")
    elif y == "4":
        print(kevins_store[4]["name"])
        print(kevins_store[4]["price"])
        print(kevins_store[4]["department"])
        print(kevins_store[4]["description"])
        print("")
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            shopping_cart.append(kevins_store[4])
            print(" ")
            print(f"{kevins_store[4]['name']} added to your cart.")
            total += 586850.00
            print(" ")
            Y = input("would you like to check out?")
        else:
            print("Item not added to cart.") 
    if Y == "yes":
        print(" ")
        print("receipt")
        print(" ")
        for item in shopping_cart:
            print(item["name"], item["price"])
            print(" ")
        print("your total is", float(total))
        break
    else:
        print(" ")