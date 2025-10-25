# Shopping Cart System (WORKING VERSION)

def add_item(cart, item_name, price, quantity):
    item = {
        "name": item_name,
        "price": price,
        "quantity": quantity
    }
    cart.append(item)
    return cart

def remove_item(cart, item_name):
    for item in cart:
        if item["name"] == item_name:
            cart.remove(item)
            print(f"{item_name} removed from cart")
            return True
    print(f"{item_name} not found in cart")
    return False

def calculate_subtotal(cart):
    subtotal = 0
    for item in cart:
        subtotal += item["price"] * item["quantity"]
    return subtotal

def apply_discount(subtotal, discount_percent):
    discount_amount = subtotal * discount_percent / 100
    final_price = subtotal - discount_amount
    return final_price

def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate
    return tax

def calculate_total(subtotal, discount, tax_rate):
    after_discount = apply_discount(subtotal, discount)
    tax = calculate_tax(after_discount, tax_rate)
    total = after_discount + tax
    return total

def display_receipt(cart, subtotal, discount, total):
    print("\n========== RECEIPT ==========")
    for item in cart:
        item_total = item["price"] * item["quantity"]
        print(f"{item['name']} x{item['quantity']} - ${item_total:.2f}")
    
    print(f"\nSubtotal: ${subtotal:.2f}")
    discount_amount = subtotal * discount / 100
    print(f"Discount ({discount}%): -${discount_amount:.2f}")
    print(f"Total: ${total:.2f}")
    print("=============================")


# Main program
print("Shopping Cart System")
print("====================")

shopping_cart = []
tax_rate = 0.08

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")
    
    choice = input("\nChoose option (1-5): ")
    
    if choice == "1":
        name = input("Item name: ")
        price = float(input("Item price: $"))
        qty = int(input("Quantity: "))
        shopping_cart = add_item(shopping_cart, name, price, qty)
        print(f"{name} added to cart")
    
    elif choice == "2":
        name = input("Item name to remove: ")
        result = remove_item(shopping_cart, name)
        if result:
            print("Item removed successfully")
    
    elif choice == "3":
        if len(shopping_cart) == 0:
            print("\nCart is empty")
        else:
            print("\nCurrent Cart:")
            for item in shopping_cart:
                print(f"- {item['name']} x{item['quantity']} @ ${item['price']:.2f} each")
    
    elif choice == "4":
        if len(shopping_cart) == 0:
            print("\nCart is empty. Add items before checkout.")
        else:
            subtotal = calculate_subtotal(shopping_cart)
            discount_percent = float(input("\nEnter discount percentage (0 if none): "))
            
            total = calculate_total(subtotal, discount_percent, tax_rate)
            
            display_receipt(shopping_cart, subtotal, discount_percent, total)
            shopping_cart = []
            print("\nThank you for your purchase!")
    
    elif choice == "5":
        print("\nGoodbye!")
        break
    
    else:
        print("\nInvalid choice")
