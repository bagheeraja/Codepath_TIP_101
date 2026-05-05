def reverse_list(lst: list[int]) -> list[any]:
    """Return a new list with the elements of lst in reverse order."""
    reverse_lst = []
    
    for i in range(len(lst) - 1, -1, -1):
        reverse_lst.append(lst[i])

    return reverse_lst

def reverse_list_slice(lst: [list]):
    #rev_lst = lst[::-1]
    return lst[::-1]

lst = [1,2,3,4,5,6,7,8,9,10]

rev_lst = reverse_list(lst)
print(rev_lst)

rev_lst2 = reverse_list_slice(lst)
print(rev_lst2)