inventory = []

def add_product():
    name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    product = {
        'name': name,
        'product_id': product_id,
        'quantity': quantity,
        'price': price
    }
    inventory.append(product)
    print(f"Product '{name}' added successfully.")

def view_inventory():
    if not inventory:
        print("No products available.")
        return
    for product in inventory:
        print(f"Name: {product['name']}, ID: {product['product_id']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")

def update_product_quantity():
    product_id = input("Enter product ID to update: ")
    new_quantity = int(input("Enter new quantity: "))
    for product in inventory:
        if product['product_id'] == product_id:
            product['quantity'] = new_quantity
            print(f"Quantity for product ID '{product_id}' updated to {new_quantity}.")
            return
    print(f"Product ID '{product_id}' not found.")

def remove_product():
    product_id = input("Enter product ID to remove: ")
    global inventory
    inventory = [product for product in inventory if product['product_id'] != product_id]
    print(f"Product ID '{product_id}' removed.")

# Start of the script
while True:
    print("\n1. Add a New Product")
    print("2. View Inventory")
    print("3. Update Product Quantity")
    print("4. Remove a Product")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_product()
    elif choice == '2':
        view_inventory()
    elif choice == '3':
        update_product_quantity()
    elif choice == '4':
        remove_product()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
