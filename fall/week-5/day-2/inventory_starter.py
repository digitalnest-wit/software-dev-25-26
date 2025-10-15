# Create inventory with items, mapping each item to a quantity
inventory = {
    "Bomb": 5,
    "Bow": 3,
    "Potion": 8,
}

print("\n=== Inventory ===")

# Display the current inventory:
# (1) TODO: Use the items() dict method to iterate over each key-value pair
# using a for-loop, printing each item and its quantity to the output.

print("\n=== Use an Item ===")

# Use an item:
# (2) TODO: Use the input() function to read the item to use from the keyboard
# and store it in item_to_use. Make sure to use the title() str method to
# capitalize the first character of this string.
item_to_use = "".title()

# Check if item exists:
# (3) TODO: Replace 'True' below with the correct conditioin to check if the
# item_to_use is in the inventory.
if True:
    # Check if quantity is greater than 0:
    # (4) TODO: Replace the 'False' below with the correct condition to check
    # if the quantity of the item_to_use is greater than 0. In other words,
    # check if there are any of this item left before trying to use it.
    if False:
        # Update the quantity:
        # (5) TODO: Update the quantity for the item_to_use in the inventory,
        # decrementing by 1.
        print(f"\nYou used {item_to_use}!")
    else:
        print(f"\nYou're out of {item_to_use}.")
else:
    print(f"\nYou don't have {item_to_use}.")

print("\n=== Updated Inventory ===")

# Display the updated inventory:
# (6) TODO: Use the items() dict method to iterate over each key-value pair
# using a for-loop, printing each item and its quantity to the output.

print(f"\nTotal item types: {len(inventory)}")
