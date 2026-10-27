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
    }
]
print("what would you like to buy?")
def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])


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
        for item in shopping_cart:
            print(item["name"], item["price"])
        print("your total is", total, "have a nice day.")
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
        else:
            print("Item not added to cart.")