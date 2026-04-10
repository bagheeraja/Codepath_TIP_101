def get_first(lst):
    if lst:
        return lst[0]
    return None

input = [3,1,6,7,5]

first_item = get_first(input)
print(first_item)