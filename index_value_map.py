def index_to_value_map(lst: list[str]) -> dict[int, str]:
    index_map = {}

    for index, item in enumerate(lst):
        index_map[index] = item

    return index_map

lst = ["apple", "banana", "cherry"]

print(index_to_value_map(lst))