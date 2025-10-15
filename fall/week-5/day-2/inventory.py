# Game Inventory Manager

print("=== Inventory ===")

# Create inventory with items
inventory = {
    "Bomb": 5,
    "Bow": 3,
    "Potion": 8,
}

# Display current inventory
for item in inventory.keys():
    print(f"  {item}: {inventory[item]}")

# Use an item
print("\n=== Use an Item ===")
item_to_use = input("Which item? ").title()

# Check if item exists
if item_to_use in inventory:
    if inventory[item_to_use] > 0:
        inventory[item_to_use] -= 1
        print(f"\nYou used {item_to_use}!")
    else:
        print(f"\nYou're out of {item_to_use}.")
else:
    print(f"\nYou don't have {item_to_use}.")

# Display updated inventory
print("\n=== Updated Inventory ===")
for item, amount in inventory.items():
    print(f"  {item}: {amount}")

print(f"\nTotal item types: {len(inventory)}")