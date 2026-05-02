def above_threshold(lst: list[int], threshold: int):
    result = []
    
    result = [num for num in lst if num > threshold]

    return result

lst = [8,2,13,11,4,10,14]

result = above_threshold(lst, 10)
print(result)
