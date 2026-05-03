def count_evens(lst: [list]):
    # list comprehension, output = expression for item in collection
    acc = 0
    
    for num in lst: 
        if num % 2 == 0:
            acc +=1

    return acc

def count_evens_bool(lst: [list]):

    return sum(num % 2 == 0 for num in lst)

lst = [1, 2, 4, 5, 7, 8, 9, 11, 12, 14, 18, 19, 20]

print(count_evens(lst))
print(count_evens_bool(lst))



