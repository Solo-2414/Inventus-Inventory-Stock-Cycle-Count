# Chocolate inventory dictionary
inventory = {
    "Item001": {"name": "Meigi", "stock": 50},
    "Item002": {"name": "Ferrero", "stock": 30},
    "Item003": {"name": "KitKat", "stock": 25},
    "Item004": {"name": "Toblerone", "stock": 46},
    "Item005": {"name": "Kisses", "stock": 30},
    "Item006": {"name": "Hersheys", "stock": 46},
    "Item007": {"name": "Snickers", "stock": 70},
    "Item008": {"name": "Cadbury", "stock": 60},
}

total_items_delivered = {}

# Function to count the physical stock sa system stock if may discrepancies
def stock_counter():
    print("--------------------------")
    for item_code, details in inventory.items():
        print(f"{item_code}: {details['name']}")
    print("--------------------------")
    item_code = input("Enter item code to check discrepancies in stock: ")

    if item_code in inventory:
        current_stock = inventory[item_code]['stock']
        print(f"Current stock for {inventory[item_code]['name']}: {current_stock}")
        actual_stock = int(input("Enter actual (physical) stock count: "))
        discrepancy = actual_stock - current_stock

        if discrepancy > 0:
            print(f"Discrepancy: {discrepancy} (overstock)")
        elif discrepancy < 0:
            print(f"Discrepancy: {discrepancy} (shortage)")
        else:
            print(f"Discrepancy: {discrepancy} (no difference)")
            return

        confirm = input("Do you want to update the system stock to match actual stock? (y/n): ").lower()

        if confirm == 'y':
            inventory[item_code]['stock'] = actual_stock
            print("Stock count updated successfully.")
        else:
            print("Stock count not updated.")
    else:
        print("Item not found.")

# Function to deliver or add something to inventory
def insert_new_delivery():
    item_code = input("Enter new item code: ")

    if item_code in inventory:
        print("Item already exists.")
        return
    
    name = input("Enter item name: ")
    stock = int(input("Enter stock count: "))
    inventory[item_code] = {"name": name, "stock": stock}
    total_items_delivered[item_code] = stock
    print("Item inserted successfully.")

# Function to remove the item to the inventory
def pull_out_item():
    print("--------------------------")
    for item_code, details in inventory.items():
        print(f"{item_code}: {details['name']}")
    print("--------------------------")

    item_code = input("Enter item code to pull out: ")

    if item_code in inventory:
        del inventory[item_code]
        print("Item pulled out successfully.")
    else:
        print("Item not found.")

# Function for looking details of specific item
def item_details():
    print("--------------------------")
    for item_code, details in inventory.items():
        print(f"{item_code}: {details['name']}")
    print("--------------------------")

    item_code = input("Enter item code: ")

    if item_code in inventory:
        item = inventory[item_code]
        print(f"Name: {item['name']}\nStock: {item['stock']}")
    else:
        print("Item not found.")

# Function of the items thats going to print kung ano ung nadeliver delivered
def show_total_items_delivered():
    print("Total Items Delivered:")
    for code, qty in total_items_delivered.items():
        print(f"{code} - {inventory.get(code, {'name': 'Unknown'})['name']}: {qty}")

# Function for printing all item in inventory
def warehouse_inventory():
    print("Warehouse Inventory:")
    for code, item in inventory.items():
        print(f"{code} - {item['name']} | Stock: {item['stock']}")

# Function for modifying ng Items.
def modify_item_details():
    print("--------------------------")
    for item_code, details in inventory.items():
        print(f"{item_code}: {details['name']}")
    print("--------------------------")

    item_code = input("Enter item code to modify: ")

    if item_code in inventory:
        item = inventory[item_code]
        print(f"\nCurrent details for {item_code}:")
        print(f"1. Name: {item['name']}")
        print(f"2. Stock: {item['stock']}")

        print("\nWhich detail do you want to modify?")
        print("1. Name")
        print("2. Stock")
        choice = input("Enter choice number: ")

        if choice == '1':
            new_name = input("Enter new name: ")
            item['name'] = new_name
            print("Name updated successfully.")
        elif choice == '2':
            new_stock = int(input("Enter new stock count: "))
            item['stock'] = new_stock
            print("Stock updated successfully.")
        else:
            print("Invalid choice.")
    else:
        print("Item not found.")

def main():
    # Menu---------------------------------
    print("|- Welcome to Inventus -|")
    while True:
        print("--------------------------")
        print("1. Stock Counter")
        print("2. Insert new Delivery")
        print("3. Pull out")
        print("4. Item Details")
        print("5. Total Items Delivered")
        print("6. Warehouse Inventory")
        print("7. Modify Item Details")
        print("8. Exit")
        choice = input("Enter choice: ")
        print("--------------------------")
    # --------------------------------------
        if choice == '1':
            stock_counter()
        elif choice == '2':
            insert_new_delivery()
        elif choice == '3':
            pull_out_item()
        elif choice == '4':
            item_details()
        elif choice == '5':
            show_total_items_delivered()
        elif choice == '6':
            warehouse_inventory()
        elif choice == '7':
            modify_item_details()
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

        cont = input("Do you want to continue (y/n)? ").lower()
        if cont != 'y':
            print("Thank you for using Inventus, Goodbye!")
            break

main()
