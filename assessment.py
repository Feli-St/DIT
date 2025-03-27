def main():
    """Main function"""
    while True:
        take_order()
        order_summary()

        print("Would you like to make another order? (Y/N)")
        choice = check_input()
            
        if choice.lower() not in ["yes", "y"]:
            print("Thank you for ordering at The Pizza Place!")
            break
        else:
            order.clear()
        
        
def take_order():
    """Takes order from user"""
    while True:
        print("Welcome to The Pizza Place.")
        display_menu()
        print("What would you like to order? (Enter 0 to exit)")

        choice = check_input()
        if choice == "0":
            break

        item = find_item(choice)
        if item:
            if "options" in item:
                size = choose_size(item["options"])
                if size:
                    order.append(
                        {
                            "name" : item["name"],
                            "size" : size,
                            "price" : item["options"][size]
                        }
                    )
            else:
                order.append(
                    {
                        "name" : item["name"],
                        "size" : None,
                        "price" : item["price"]
                    }
                )
        else:
            print("Sorry that item is not on the menu.")




def check_input():
    """Check if input is not empty"""
    while True:
        choice = input(">")
        if choice:
            break
        else:
            print("Invalid input")
    return choice




def display_menu():
    """Formats and displays menu to the user"""
    print("\n--- MENU ---")
    for category, items in menu.items():
        print(f"\n{category}:")
        for item in items:
            if "options" in item:
                print(f"    {item['name']}:")
                for size, price in item["options"].items():
                    print(f"        {size} - ${price:.2f}")
            else:
                print(f"    {item['name']} - ${item['price']:.2f}")
    return


def choose_size(options):
    """Lets the user choose the size they want"""
    print("Available sizes:")
    for size in options:
        print(f"- {size}")

    while True:
        size_choice = input("Choose a size: ").lower()
        if size_choice in options:
            return size_choice
        else: 
            print("Invalid size")


def find_item(choice):
    """Finds an item in the menu and returns it"""
    for category, items in menu.items():
        for item in items:
            if choice.lower() == item["name"].lower():
                return item
    return None


def format_order(item):
    """Format order for display"""
    if item["size"]:
        return f"{item['name']} ({item['size']}) - ${item['price']:.2f}"
    else:
        return f"{item['name']} - ${item['price']:.2f}"
    


def order_summary():
    """Display final order and total price"""
    if not order:
        print("\nNo items ordered.")
        return
    
    print("\nYour final order:")
    total_price = 0
    for item in order:
        print(f"- {format_order(item)}")
        total_price += item["price"]
    print(f"\nTotal price: ${total_price:.2f}")


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



