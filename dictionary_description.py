def get_description(info: dict[str,str | int], keys: list[str]):
    for key in keys:
        value = info.get(key)
        print(value)

info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]

get_description(info, keys)