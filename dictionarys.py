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
    def choose_item():
        show_items(kevins_store)
        x = int(input("Which item number do you want to buy? or enter shopping cart to check your items"))
        print(kevins_store[x])
        shopping_cart.append(kevins_store[x])
    
    choose_item()
        
    y = input("are you done shopping? Type Y to enter check your shopping cart and N to continue shopping")
    if y == "Y":
        total += sum(item["price"] for item in shopping_cart)
        print("Your shopping cart")
        if shopping_cart:
            for item in shopping_cart:
                print(item["name"], item["price"])
                print(" ")
            else:
                print("Your cart is empty.")   

            z = input("would you like to check out?")
            if z == "yes":
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
    elif y == "N":
        total += sum(item["price"] for item in shopping_cart)

        
        

    

    