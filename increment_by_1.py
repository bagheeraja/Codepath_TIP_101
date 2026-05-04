def increment_values(lst: [list]):
    # return the list incremented by one
    # list comprehension is expression for item in collection
    return [(num + 1) for num in lst]

def increment_values_append(lst: [list]):
    new_lst = []
    
    for num in lst:
        new_lst.append(num + 1)

    return new_lst


lst = [3,5,8,2]
new_lst = increment_values(lst)
new_lst_2 = increment_values_append(lst)
print(new_lst)
print(new_lst_2)
