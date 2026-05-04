def check_num(lst: list[int], num: int) -> bool:

    return num in lst

lst = [5,2,3,9,10]
flag1 = check_num(lst, 9)
flag2 = check_num(lst, 4)

print(flag1)
print(flag2)

