# -----------------------------------------------------------
# SEAN VENDING MACHINE PRO MAX PLUS 
# -----------------------------------------------------------
# This Program demonstrates knowledge of programming and 
# techniques gathered over the course of the module in 
# developing a python program language to simulate a 
# console-based Vending Machine.
# -----------------------------------------------------------

# Nested dictionary for categorized inventory management.
inventory = {
    "Drinks ♪(´▽｀)": {
        "A1": {"title": "Water", "cost": 2.0, "stock": 5},
        "A2": {"title": "Cola", "cost": 3.0, "stock": 4},
        "A3": {"title": "Juice", "cost": 3.5, "stock": 3},
        "A4": {"title": "Coffee", "cost": 4.0, "stock": 5}
    },
    "Snacks(｡･∀･)ﾉﾞ": {
        "B1": {"title": "Chocolate", "cost": 2.5, "stock": 5},
        "B2": {"title": "Chips", "cost": 3.0, "stock": 2},
        "B3": {"title": "Biscuits", "cost": 2.0, "stock": 4},
        "B4": {"title": "Popcorn", "cost": 3.5, "stock": 3}
    }
}

# Relational mapping for the recommendation system.
recommendations = {
    "Chocolate": "Water", "Chips": "Cola", "Biscuits": "Coffee", "Popcorn": "Juice",
    "Water": "Biscuits", "Cola": "Chips", "Juice": "Popcorn", "Coffee": "Chocolate"
}

def display_menu():
    print("\n" + "=" * 40 + "☆")
    for category, products in inventory.items():
        print(f"\n[{category}]")
        for code, details in products.items():
            # Dynamic stock evaluation for menu rendering.
            if details["stock"] > 0:
                print(f" {code}: {details['title']} ({details['cost']} AED | Stock: {details['stock']})")
            else:
                print(f" {code}: {details['title']} (SOLD OUT)")
    print("\n" + "=" * 40 + "☆")

def find_item(code):
    # Search logic for locating keys within nested values.
    for group in inventory.values():
        if code in group:
            return group[code]
    return None

def suggest_item(item_name):
    if item_name in recommendations:
        print(f"\n[Note] Recommendation: {recommendations[item_name]} taste even better with {item_name}.!!")

# Function to generate and print the purchase receipt
def receipt_maker(item_name, cost, paid, change):
    print("\n" + "*" * 35)
    print("      ☆ PURCHASE RECEIPT ☆      ")
    print("*" * 35)
    print(f" Item:       {item_name}")
    print(f" Cost:       {cost} AED")
    print(f" Paid:       {paid} AED")
    print(f" Change:     {change} AED")
    print("*" * 35)
    print(" Thank you for ur purchase! ദ്ദി◝ ⩊ ◜.ᐟ ")
    print("*" * 35)

def process_payment(cost):
    try:
        payment = float(input("Insert cash (AED): "))
    except ValueError:
        # Exception handling to prevent runtime errors from invalid input types.
        print("\n[!] INPUT ERROR: Please enter numeric values only.")
        return None, None

    if payment <= 0:
        print("\n[!] INVALID PAYMENT: Amount must be positive.")
        return None, None
    if payment < cost:
        print("[!] INSUFFICIENT FUNDS: Transaction cancelled.")
        return None, None

    # Currency precision using the round function.
    change = round(payment - cost, 2)
    return change, payment

def vending_machine():
    print("--- SEAN VENDING MACHINE PRO MAX PLUS ---")

    while True:
        display_menu()

        # Input normalization for case-insensitivity.
        user_pick = input("\nEnter item code or 'exit': ").upper()

        if user_pick == "EXIT":
            print("\nShutting down... Thank you for using Sean Vending Machine Pro Max! /(ㄒoㄒ)/~~")
            break

        selected = find_item(user_pick)

        if not selected:
            print("\n[!] INVALID CODE: Please try again.")
            continue

        if selected["stock"] <= 0:
            print(f"\n[!] OUT OF STOCK: {selected['title']} is unavailable.")
            continue

        suggest_item(selected["title"])

        print(f"\nSelected: {selected['title']} | Cost: {selected['cost']} AED")

        change, paid = process_payment(selected["cost"])
        if change is None:
            continue

        # State update: decrementing inventory stock levels.
        selected["stock"] -= 1
        print(f"\n✔ Success! {selected['title']} has been dispensed.")

        # Call the receipt maker function
        receipt_maker(selected['title'], selected['cost'], paid, change)

        again = input("\nWould you like to buy another item? (yes/no): ").lower()
        if again != "yes":
            print("\nThank you for using Sean Vending Machine Pro Max (๑•̀ㅂ•́)و✧!")
            break
        
vending_machine()