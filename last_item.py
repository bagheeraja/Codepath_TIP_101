def get_last(lst):
    if lst:
        return lst[len(lst) - 1]
    else:
        return None
    
list_1 = [3,1,6,7,5]

print(get_last(list_1))