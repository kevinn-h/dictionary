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
while True:
   
    y = input("Choose an item number, type 'shopping cart', or 'quit': ")

    if y == "shopping cart":
        print("Your shopping cart")
        if shopping_cart:
            for item in shopping_cart:
                print(f"{item['name']} {item['price']}")
        else:
            print("Your cart is empty.")
    elif y == "quit":
        print("Goodbye!")
        break

    elif y == "0":
        print(kevins_store[0]["name"])
        print(kevins_store[0]["price"])
        print(kevins_store[0]["department"])
        print(kevins_store[0]["description"])
        z = input("Would you like to buy this item? ")
        if z == "yes":
            shopping_cart.append(kevins_store[0])
            print(f"{kevins_store[0]['name']} added to your cart.")
        else:
            print("Item not added to cart.")
    else:
        print("Invalid choice, Please choose a valid item number or command.")