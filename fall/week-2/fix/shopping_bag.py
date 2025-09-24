# Shopping Cart Discount Calculator - COMPLETE VERSION
# This program calculates discounts based on membership status and cart total

print("🛒 Welcome to Digital NEST Store! 🛒")
print()

# Get user input
name = input("Enter your name: ")
membership = input("Are you a member? (yes/no): ").lower()
cart_total = float(input("Enter your cart total: $"))

print()
print(f"Processing order for {name}...")

# Initialize discount variables
discount_percent = 0
discount_reason = ""

# Determine discount based on membership and cart total
if membership == "yes":
    if cart_total >= 100:
        discount_percent = 20
        discount_reason = "VIP Member (20% off orders $100+)"
    elif cart_total >= 50:
        discount_percent = 15
        discount_reason = "Member (15% off orders $50+)"
    else:
        discount_percent = 10
        discount_reason = "Member (10% off all orders)"
else:
    if cart_total >= 75:
        discount_percent = 5
        discount_reason = "New Customer (5% off orders $75+)"
    else:
        discount_percent = 0
        discount_reason = "No discount available"

# Calculate final amounts
discount_amount = cart_total * (discount_percent / 100)
final_total = cart_total - discount_amount

# Display results
results = f'''
{"=" * 40}
"ORDER SUMMARY"
{"=" * 40}
Customer: {name}
Member: {'Yes' if membership == 'yes' else 'No'}
Original Total: ${cart_total:.2f}
Discount Applied: {discount_reason}
Discount Amount: ${discount_amount:.2f}
Final Total: ${final_total:.2f}
{"=" * 40}
'''

print(results)

# Thank you message
if discount_percent > 0:
    print(f"🎉 You saved ${discount_amount:.2f}!")
else:
    print("💡 Tip: Become a member to save on all orders!")

print("Thank you for shopping with us! 😊")
