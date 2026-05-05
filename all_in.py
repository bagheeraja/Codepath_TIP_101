def all_in(a: list[int], b: list[int]) -> bool:
    # Understand - are the lists sorted, what if both lists are empty, will list b always be longer than list a
    # Plan - compare length. if necessary, sort lists. compare indices. if all match by the end of a return True, if not return False
    # Implement
    #compare length
    if len(b) < len(a):
        return False
    
    for item in a:
        if item in b:
            continue
        return False
    return True



lst_1 = [1,2]
lst_2 = [1,2,3]

print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))


    
