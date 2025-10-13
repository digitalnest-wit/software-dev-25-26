# Shopping List Program

shopping_list = []

print("Shopping List Creator")
print("Enter items for your shopping list.")
print()

# Collect items from user
num_items = int(input("How many items do you need? "))

for i in range(num_items):
    item = input(f"Enter item {i + 1}: ")
    shopping_list.append(item)

# Display complete shopping list
print("\n--- Your Shopping List ---")

for i, item in enumerate(shopping_list):
    print(f"{i + 1}. {item}")

print(f"\nTotal items: {len(shopping_list)}")
