def flip_signs(lst: [list]):
    # list comprehesnion expression for item in colleciton
    return [(num * -1) for num in lst]

lst = [1, -2, -3, 4, 5, 6, -7, -8]

print(flip_signs(lst))