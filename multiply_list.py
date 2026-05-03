def multiply_list(lst: [list], multiplier: [int]):
    new_lst = []

    for num in lst:
        new_lst.append(num * multiplier)
    
    return new_lst

def multiply_list_comprehension(lst: [list], multiplier: [int]):

    # return [expression for item in collection]
    return [(num * multiplier) for num in lst]

lst = [1,2,3,4,5,6]

print(multiply_list(lst, 8))

print(multiply_list_comprehension(lst, 12))