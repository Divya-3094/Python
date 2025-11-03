# shopping_cart.py

# Predefined products
products = [
    {"id": 1, "name": "Laptop", "price": 45000},
    {"id": 2, "name": "Smartphone", "price": 15000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Keyboard", "price": 1200},
    {"id": 5, "name": "Mouse", "price": 800},
    {"id": 6, "name": "Charger", "price": 500},
    {"id": 7, "name": "USB Cable", "price": 300},
    {"id": 8, "name": "Backpack", "price": 2500}
]

# Initialize empty cart
cart = []


# Function to view all products
def view_products(products):
    print("\n===== Available Products =====")
    for product in products:
        print(f"ID: {product['id']} | {product['name']} - ₹{product['price']}")
    print("==============================")


# Function to add product to cart
def add_to_cart(products, cart, product_id, quantity):
    # Check cart limit (max 8 items)
    if len(cart) >= 8:
        print("⚠ Cart is full (Max 8 items).")
        return

    # Find product
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        print("❌ Invalid Product ID.")
        return

    # Check if product already in cart
    for item in cart:
        if item["id"] == product_id:
            item["quantity"] += quantity
            print(f"✔ Updated {product['name']} quantity to {item['quantity']}.")
            return

    # Add new item
    cart.append({
        "id": product["id"],
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    })
    print(f"✔ {product['name']} added to cart.")


# Function to view cart
def view_cart(cart):
    if not cart:
        print("\n🛒 Cart is empty.")
        return

    print("\n===== Your Cart =====")
    total = 0
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
    print(f"-----------------------\nTotal: ₹{total}")
    print("======================")


# Function to update quantity in cart
def update_cart(cart, product_id, quantity):
    for item in cart:
        if item["id"] == product_id:
            item["quantity"] = quantity
            print(f"✔ Quantity updated for {item['name']} to {quantity}.")
            return
    print("❌ Item not found in cart.")


# Function to remove item from cart
def remove_from_cart(cart, product_id):
    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            print(f"✔ {item['name']} removed from cart.")
            return
    print("❌ Item not found in cart.")


# Function to checkout
def checkout(cart):
    if not cart:
        print("\n🛒 Cart is empty.")
        return

    print("\n===== Checkout =====")
    total = 0
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
    print(f"-----------------------\nFinal Total: ₹{total}")
    print("🎉 Thank you for shopping with us!")

    # Empty cart after checkout
    cart.clear()


# Menu function
def menu():
    while True:
        print("\n===== Shopping Cart =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_products(products)

        elif choice == "2":
            try:
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))
                add_to_cart(products, cart, product_id, quantity)
            except ValueError:
                print("❌ Invalid input. Please enter numbers.")

        elif choice == "3":
            view_cart(cart)

        elif choice == "4":
            try:
                product_id = int(input("Enter Product ID to update: "))
                quantity = int(input("Enter new Quantity: "))
                update_cart(cart, product_id, quantity)
            except ValueError:
                print("❌ Invalid input. Please enter numbers.")

        elif choice == "5":
            try:
                product_id = int(input("Enter Product ID to remove: "))
                remove_from_cart(cart, product_id)
            except ValueError:
                print("❌ Invalid input. Please enter numbers.")

        elif choice == "6":
            checkout(cart)

        elif choice == "7":
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    menu()
