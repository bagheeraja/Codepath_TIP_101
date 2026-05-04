def doubled(lst: [list]):
    # list comprehension expression for item in collection
    return [(num * 2) for num in lst]

lst = [1, 2, 3, 4, 5, 6, 7]

print(doubled(lst))