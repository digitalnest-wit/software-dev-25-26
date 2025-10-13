# Inventory System - BUGGY VERSION
# This program has multiple list-related bugs to debug

inventory = ["laptop", "mouse", "keyboard"]
quantities = [5, 12, 8]

print("=== Inventory Management System ===\n")

# Display initial inventory
print("Current Inventory:")
for i in range(len(inventory)):
    print(f"{i}. {inventory[i]}: {quantities[i]} units")

print("\n--- Adding New Products ---")

# Bug 1: IndexError - trying to access index that doesn't exist
new_product = "monitor"
new_quantity = 7
inventory.append(new_product)
quantities.append(new_quantity)
print(f"Added: {inventory[3]}: {quantities[4]} units")  # Bug: quantities[4] doesn't exist

print("\n--- Removing Out of Stock Items ---")

# Bug 2: Modifying list while iterating
for item in inventory:
    if item == "mouse":
        inventory.remove(item)  # Bug: modifying list during iteration
        quantities.pop(1)
        print(f"Removed: {item}")

print("\n--- Sorting Inventory ---")

# Bug 3: Methods returning None
sorted_inventory = inventory.sort()  # Bug: sort() returns None
print(f"Sorted inventory: {sorted_inventory}")

print("\n--- Updating Quantities ---")

# Bug 4: Using wrong index
quantities[3] = 15  # Bug: may cause IndexError depending on list length
print(f"Updated quantities: {quantities}")

print("\n--- Finding Products ---")

# Bug 5: Not checking if item exists before using index()
search_item = "tablet"
position = inventory.index(search_item)  # Bug: will crash if not found
print(f"{search_item} found at position {position}")

print("\n--- Final Inventory ---")

# Bug 6: Confusing remove() with pop()
inventory.remove(0)  # Bug: tries to remove value 0, not index 0
quantities.remove(0)

for i in range(len(inventory)):
    print(f"{i + 1}. {inventory[i]}: {quantities[i]} units")
