def merge_catalogs(catalog1: dict[str, float], catalog2: dict[str, float]) -> dict[str, float]:
    for item, price in catalog2.items():
        catalog1[item] = price
    return catalog1

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}

print(merge_catalogs(catalog1, catalog2))