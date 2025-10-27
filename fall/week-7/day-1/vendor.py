from time import sleep

def load_vendor_items() -> list[dict]:
    items = []

    with open(file="vendor.txt", mode="r") as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.split(",")
        name, price, amount = tuple(line)
        
        item = {
            "name": name,
            "price": float(price),
            "amount": int(amount),
        }
        
        items.append(item)
    
    return items

def update_vendor_items(items: list[dict]):    
    with open(file="vendor.txt", mode="w") as f:
        for item in items:
            name, price, amount = tuple(item.values())
            f.write(f"{name},{price},{amount}\n")


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
