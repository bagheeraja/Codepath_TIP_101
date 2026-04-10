def print_negatives(lst):
    if lst:
        res = []
        for num in lst:
            if num < 0:
                res.append(num)
        return(res)
    else:
        return None

list_1 = [3,-2,2,-1,1,-5]

print(print_negatives(list_1))
