def get_items_to_restock(products: dict[str,int], restock_threshold: int) -> list[str]:
    restock_list = []

    for key, value in products.items():
        if value < restock_threshold:
            restock_list.append(key)
    return restock_list

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5

print(get_items_to_restock(products, restock_threshold))
