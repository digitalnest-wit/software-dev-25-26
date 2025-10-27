from time import sleep

def load_vendor_items() -> list[dict]:
    """Returns a list with the items in the vendor file.

    Returns:
        list[dict]: The items listed in the vendor file.
    """
    raise NotImplementedError

def update_vendor_items(items: list[dict]):    
    """Updates the vendor file, replacing its contents with items.

    Args:
        items (list[dict]): The updated vendor items.
    """
    raise NotImplementedError

vendor_items = load_vendor_items()

print("Make a selection:")

for i, item in enumerate(vendor_items):
    if item["amount"] == 0:
        continue
    
    print(f"  {i + 1}: {item["name"]} @ ${item["price"]:.2f}")

selection = int(input("\n> Selection: "))
if selection < 1 or selection > len(vendor_items):
    print("Bad selection. Try again.")
else:
    item_selected = vendor_items[selection - 1]
    print(f"Selected {item_selected["name"]}. Vending..")
    
    sleep(1)
    item_selected["amount"] -= 1
    update_vendor_items(vendor_items)
    
    print("Done! Enjoy :)")
