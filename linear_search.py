def linear_search(lst: [int], target: int):
    for i, n in enumerate(lst):
        if n == target:
            return i
    return -1

lst = [1,4,5,2,8]

position = linear_search(lst, 5)
print(position)

position = linear_search(lst, 10)
print(position)
