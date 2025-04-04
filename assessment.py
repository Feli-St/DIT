import re


def main():
    """Main function"""
    while True:
        take_order()
        if order["items"]:
            choose_order_type()
        order_summary()
        #export_order(order, r"C:\Users\felis\Documents")

        print("Would you like to make another order? (Y/N)")
        choice = check_input()
            
        if choice.lower() not in ["yes", "y"]:
            print("Thank you for ordering at The Pizza Place!")
            break
        else:
            reset_order()
        
        
def take_order():
    """Takes order from user"""
    while True:
        print("\nWelcome to The Pizza Place!")
        display_menu()
        print("What would you like to order? (Enter 0 to exit)")

        choice = check_input()
        if choice == "0":
            break

        item = find_item(choice)
        print("How many would you like?")
        amount = check_int(1)

        if item:
            if "options" in item:
                size = choose_size(item["options"])
                
                order_item = is_in_order(item["name"], size)
                if order_item:
                    order_item["amount"] += amount
                
                else:
                    if size:
                        order["items"].append(
                            {
                                "name" : item["name"],
                                "size" : size,
                                "price" : item["options"][size],
                                "amount" : amount
                            }
                        )
                print(f"{amount}x {item['name']} ({size}) has been added to your order.")
            else:

                order_item = is_in_order(item["name"])
                if order_item:
                    order_item["amount"] += amount
                else:
                    order["items"].append(
                        {
                            "name" : item["name"],
                            "size" : None,
                            "price" : item["price"],
                            "amount" : amount
                        }
                    )
                print(f"{amount}x {item['name']} has been added to your order.")
        else:
            print("Sorry that item is not on the menu.")




def check_input():
    """Check if input is not empty"""
    while True:
        choice = input(">").strip()
        if choice:
            break
        else:
            print("Invalid input")
    return choice


def check_int(min):
    """Check if input is an integer and bigger than a minimum"""
    while True:
        try:
            choice = int(input(">"))
            if choice >= min:
                return choice
            else:
                print(f"Please enter a number bigger than or equal to {min}")
        except ValueError:
            print("Please enter an integer")



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


def is_in_order(choice, size=None):
    for item in order["items"]:
        if item["size"]:
          if choice.lower() == item["name"].lower() and item["size"].lower() == size.lower():  
              return item
        else:
            if choice.lower() == item["name"].lower():
                return item
    return None


def format_order(item):
    """Format order for display"""
    if item["size"]:
        return f"{item['amount']}x {item['name']} ({item['size']}) - ${item['price']:.2f}"
    else:
        return f"{item['amount']}x {item['name']} - ${item['price']:.2f}"
    


def order_summary():
    """Display final order and total price"""
    if not order["items"]:
        print("\nNo items ordered.")
        return
    
    print("\n--- ORDER SUMMARY ---")
    print(f"Order Type: {order['order_type'].capitalize()}")

    print("Customer Information:")

    for x, y in order["customer_info"].items():
        print(f"    {x.capitalize()}: {y}")

    print("\nItems ordered:")
    total_price = 0
    for item in order["items"]:
        print(f"- {format_order(item)}")
        total_price += item["price"] * item["amount"]
    if order["order_type"] == "delivery":
        print(f"\nDelivery charge: ${DELIVERY_CHARGE:.2f}")
        total_price += DELIVERY_CHARGE
    
    order['total'] = total_price

    print(f"\nTotal price: ${total_price:.2f}")



def choose_order_type():
    """Ask the user to choose between pickup and delivery"""
    print("\nWould you like to pick up your delivery of have it delivered? (pickup/delivery)")
    while True:
        choice = check_input().lower()
        if choice in ["pickup", "delivery"]:
            order["order_type"] = choice
            break
        else:
            print("Please pick between delivery or pickup.")

    if choice == "delivery":
        get_user_info()
    else: 
        while True:
            name = input("Please enter your full name: ")
            if len(name.split()) >= 2:
                order["customer_info"] = {"name" : name}
                break
            else:
                print("Please enter both your first and last name.")
    return
    

def get_user_info():
    """Get customer details for delivery"""
    print("\nPlease provide your delivery details.")

    while True:
        name = input("Full name: ").strip()
        if len(name.split()) >= 2:
            break
        print("Please enter your full name.")

    while True:
        phone = input("Phone number: ").strip()
        if re.fullmatch(r"[\d\s\-+()]+", phone) and len(phone) >= 7:
            break
        print("Please enter a valid phone number (7 digits, numbers only).")

    while True:
        address = input("Delivery address: ").strip()
        if address:
            break
        print("Address cannot be empty.")


    order["customer_info"] = {
        "name" : name,
        "phone" : phone,
        "address" : address
    }


def reset_order():
    """Resets order for new session"""
    order["order_type"] = None
    order["customer_info"] = {}
    order["items"] = []


def export_order(order, filename="order.txt"):
    with open(filename, "w") as file:
        file.write("Order Summary\n-------------\n")
        file.write(f"Customer: {order['customer_info']['name']}\n")
        file.write(f"Pickup or Delivery: {order['order_type']}\n")

        if order["order_type"] == "delivery":
            file.write(f"Phone: {order['customer_info']['phone']}\n")
            file.write(f"Address: {order['customer_info']['address']}\n")
        
        file.write("\nItems Ordered:\n")
        
        for item in order["items"]:
            formatted_item = format_order(item)
            file.write(f"- {formatted_item}\n")

        file.write(f"\nTotal: ${order['total']:.2f}\n")

    
    
DELIVERY_CHARGE = 5

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



order = {
    "order_type" : None,
    "customer_info" : {},
    "items" : [],
    "total" : 0
}

main()



