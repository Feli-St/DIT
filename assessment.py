def main():
    while True:
        print("Welcome to The Pizza Place.")
        display_menu()
        print("What would you like to order?")
        choice = check_input()
        if choice == "0":
            break
        
        print(order)
    return


def check_input():
    while True:
        choice = input(">")
        if choice:
            break
        else:
            print("Invalid input")
    return choice




def display_menu():
    for category, items in menu.items():
        print(category)
        for x, y in items.items():
            if type(items[x]) == float:
                print(f"{x} : {items[x]}")
            else:
                print(x)
                for z in y:
                    print(f"{z} : {y[z]}")


    return

menu = {
    "Pizza": [
        {"name": "Margherita", "options": {"small": 14.99, "medium": 19.98}},
        {"name": "Meat Lovers", "options": {"small": 21.99, "medium": 26.98}},
        {"name": "Beef & Onion", "options": {"small": 15.49, "medium": 20.49}},
        {"name": "Veggie Lovers", "options": {"small": 17.49, "medium": 22.48}},
    ],
    "Sides": [
        {"name": "Garlic Bread", "price": 5.99},
        {"name": "Fries", "price": 6.49},
    ],
    "Sauces": [
        {"name": "Tomato sauce", "price": 0.59},
        {"name": "Aioli sauce", "price": 0.59},
        {"name": "BBQ sauce", "price": 0.59},
    ],
}



order = []
main()



