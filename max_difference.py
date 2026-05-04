def max_difference(lst: [list]):
    # return the difference between the smallest and largest value in the field
    return max(lst) - min(lst)

def max_difference_loop(lst: [list]):
    max = lst[0]
    min = lst[0]
    
    for num in lst:
        if num > max:
            max = num
        elif num < min:
            min = num
    return max - min


lst = [5,22,8,10,2]

print(max_difference(lst))
print(max_difference_loop(lst))