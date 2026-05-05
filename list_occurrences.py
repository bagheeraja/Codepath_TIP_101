def find_all_occurrences(lst: list[int], target: int) -> list[int]:
    indices = []
    
    for i in range(len(lst)):
        if lst[i] == target:
            indices.append(i)
    return indices

def find_all_occurrences_enum(lst: list[int], target: int) -> list[int]:
    """Returns a list of indices where the target exists submitted lst"""
    
    indices = []
    
    for i, n in enumerate(lst):
        if n == target:
            indices.append(i)
    return indices



lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)

index_list_2 = find_all_occurrences_enum(lst, 3)
print(index_list_2)
