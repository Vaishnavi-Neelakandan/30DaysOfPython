# Day 3: Fruit Shop Inventory System with Billing

# Purchased items (cart)
Purchased_fruits = {}

# Fruits inventory
fruits_inventory = {
    "apple": {"qty": 10, "price": 6.99},
    "banana": {"qty": 20, "price": 0.69},
    "orange": {"qty": 10, "price": 5.99},
    "avocado": {"qty": 20, "price": 5.47},
    "watermelon": {"qty": 30, "price": 5.99},
    "blueberries": {"qty": 5, "price": 4.47}
}

# Show inventory
def display_fruits():
    print("\nAvailable fruits:")
    print("------------------------------------------------")
    print("Fruit       | Price (₹) | Qty  | Stock Status")
    print("------------------------------------------------")
    for fruit, data in fruits_inventory.items():   #Iterates over each fruit and its corresponding qty and price (which is a nested dictionary).
        qty = data["qty"]          #Extracts qty for each fruit
        price = data["price"]      #Extracts price for each fruit
        status = f"{qty} in stock" if qty > 0 else "Out of stock"  #Prints the quantity if its greater than 0 else prints out of stock
        print(f"{fruit.capitalize():<12} ₹{price:<9} {qty:<5} {status}") #:<number left aligns the name to the specified character space
    print("------------------------------------------------")

# Buy fruit and update stoc and add the item to cart
def buy_fruits():
    fruits = input("\nEnter the fruit name: ").lower()

    if fruits in fruits_inventory:
        try:
            qty = int(input(f"How many {fruits} do you want to buy? "))
            available = fruits_inventory[fruits]["qty"]
            price = fruits_inventory[fruits]["price"]

            if qty <= available:
                # Update stock in inventory
                fruits_inventory[fruits]["qty"] -= qty

                # Add to cart or update existing entry
                if fruits in Purchased_fruits:
                    Purchased_fruits[fruits]["qty"] += qty
                    Purchased_fruits[fruits]["total"] += qty * price
                else:
                    Purchased_fruits[fruits] = {
                        "qty": qty,
                        "price": price,
                        "total": qty * price
                    }

                print(f"You bought {qty} {fruits} for ₹{qty * price}.")
            else:
                print(f"Only {available} {fruits} available in stock.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"Fruit '{fruits}' not available in shop.")


# Show bill
def show_bill():
    if not Purchased_fruits:
        print("\n Your cart is empty.")
        return

    print("\n Your Bill:")
    print("-------------------------------------------")
    print("Fruit        Qty   Price   Total")
    print("-------------------------------------------")
    
    total_amount = 0
    for fruit, data in Purchased_fruits.items():
        qty = data["qty"]
        price = data["price"]
        total = data["total"]
        print(f"{fruit.capitalize():<12} {qty:<5} ₹{price:<6} ₹{total:.2f}")
        total_amount += total
    print("-------------------------------------------")
    print(f"Total Amount to Pay: ₹{total_amount:.2f}")

# Main menu
while True:
    print("\n========== Fruit Shop Menu ==========")
    print("1. Fruits List")
    print("2. Buy Fruit")
    print("3. View Bill")
    print("4. Exit")
    print("=====================================")

    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == "1":
        display_fruits()
    elif choice == "2":
        buy_fruits()
    elif choice == "3":
        show_bill()
    elif choice == "4":
        show_bill()
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")
