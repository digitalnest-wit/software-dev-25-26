# Inventory System

inventory = ["laptop", "mouse", "keyboard"]
quantities = [5, 12, 8]

print("=== Inventory Management System ===\n")

# Display initial inventory
print("Current Inventory:")
for i in range(len(inventory)):
    print(f"{i}. {inventory[i]}: {quantities[i]} units")

print("\n--- Adding New Products ---")

# Fix 1: Use correct index after appending
new_product = "monitor"
new_quantity = 7
inventory.append(new_product)
quantities.append(new_quantity)
print(f"Added: {inventory[-1]}: {quantities[-1]} units")  # Fixed: use -1 or len()-1

print("\n--- Removing Out of Stock Items ---")

# Fix 2: Create a copy to iterate over, or iterate backwards
item_to_remove = "mouse"
if item_to_remove in inventory:
    index = inventory.index(item_to_remove)
    inventory.pop(index)  # Fixed: remove from original while iterating over copy
    quantities.pop(index)
    print(f"Removed: {item_to_remove}")

print("\n--- Sorting Inventory ---")

# Fix 3: sort() modifies in place and returns None
inventory.sort()  # Fixed: don't assign result
print(f"Sorted inventory: {inventory}")

print("\n--- Updating Quantities ---")

# Fix 4: Check valid index or use safe indexing
if len(quantities) > 2:  # Fixed: check bounds before accessing
    quantities[2] = 15
    print(f"Updated quantities: {quantities}")

print("\n--- Finding Products ---")

# Fix 5: Check if item exists before using index()
search_item = "tablet"
if search_item in inventory:  # Fixed: check existence first
    position = inventory.index(search_item)
    print(f"{search_item} found at position {position}")
else:
    print(f"{search_item} not found in inventory")

print("\n--- Final Inventory ---")

# Fix 6: Use pop() with index, not remove() with index
if len(inventory) > 0:  # Fixed: check if list has items
    inventory.pop(0)  # Fixed: use pop() to remove by index
    quantities.pop(0)

for i in range(len(inventory)):
    print(f"{i + 1}. {inventory[i]}: {quantities[i]} units")