def restock_inventory(current_inventory: dict[str, int], restock_list: dict[str, int]) -> dict[str, int]:
    for item, amount in restock_list.items():
        current_inventory[item] = current_inventory.get(item, 0) + amount
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))