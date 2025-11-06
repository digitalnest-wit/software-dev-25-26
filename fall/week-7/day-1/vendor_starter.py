from time import sleep

def load_vendor_items() -> list[dict]:
    """Returns a list with the items in the vendor file.

    Returns:
        list[dict]: The items listed in the vendor file.
    """
    
    items = []

    with open("vendor.txt") as file:
        lines = file.readlines()

    for line in lines:
        line = line.split(",")
        name, price, amount = line
        
        item = {
            "name": name,
            "price": float(price),
            "amount": int(amount),
        }
        
        items.append(item)

    return items
    
    
def update_vendor_items(items: list[dict]):
    with open("vendor.txt", mode="w") as file:
        for item in items:
            name, price, amount = item.values()
            file.write(f"{name},{price},{amount}\n")

