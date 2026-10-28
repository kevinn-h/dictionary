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
        "name": "16 GB DDR5 RAM",
        "price": 1055.99,
        "department": "electronics",
        "description": "very very very gud ram for computa"


    },
    {

        "name": "williams shoe",
        "price": 200.50,
        "department": "trash",
        "description": "very famous shoe but very smelly"
    },
    {

    "name": "Aiden's Roblox Account"
    ,"price": 100.00,
    "department": "Video Games",
    "description": "100 BILLION robux inside and 1600 wins on bedwars"
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
    "description": "aidens house"
    }
]


def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])
show_items(kevins_store)

shopping_cart = []
total = 0
while True:
    y = input("Choose an item number, type 'shopping cart', 'checkout', or 'quit': ")
    if y == "shopping cart":
        print("Your shopping cart")
        if shopping_cart:
            for item in shopping_cart:
                print(item["name"], item["price"])
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
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            shopping_cart.append(kevins_store[0])
            print(f"{kevins_store[0]['name']} added to your cart.")
            total +=1055.99
            Y = input("would you like to check out?")
        else:
            print("Item not added to cart.")
    elif y == "1":
        print(kevins_store[1]["name"])
        print(kevins_store[1]["price"])
        print(kevins_store[1]["department"])
        print(kevins_store[1]["description"])
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            shopping_cart.append(kevins_store[1])
            print(f"{kevins_store[1]['name']} added to your cart.")
            total += 200.50
            Y = input("would you like to check out?")
        else:
            print("Item not added to cart.")
    elif y == "2":
        print(kevins_store[2]["name"])
        print(kevins_store[2]["price"])
        print(kevins_store[2]["department"])
        print(kevins_store[2]["description"])
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            shopping_cart.append(kevins_store[2])
            print(f"{kevins_store[2]['name']} added to your cart.")
            total += 100
            Y = input("would you like to check out?")
        else:
            print("Item not added to cart.")
    elif y == "3":
        print(kevins_store[3]["name"])
        print(kevins_store[3]["price"])
        print(kevins_store[3]["department"])
        print(kevins_store[3]["description"])
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            shopping_cart.append(kevins_store[3])
            print(f"{kevins_store[3]['name']} added to your cart.")
            total += 316850.00
            Y = input("would you like to check out?")
        else:
            print("Item not added to cart.")
    elif y == "4":
        print(kevins_store[4]["name"])
        print(kevins_store[4]["price"])
        print(kevins_store[4]["department"])
        print(kevins_store[4]["description"])
        z = input("Would you like to buy this item? ")
        if z.lower() == "yes":
            shopping_cart.append(kevins_store[4])
            print(f"{kevins_store[4]['name']} added to your cart.")
            total += 586850.00
            Y = input("would you like to check out?")
        else:
            print("Item not added to cart.") 
    if Y == "yes":
        print("receipt")
        for item in shopping_cart:
            print(item["name"], item["price"])
            print("your total is", float(total))
            break