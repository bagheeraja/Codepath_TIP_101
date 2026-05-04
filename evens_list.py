def get_evens(lst: [list]):
    # return a list of all even numbers in the list
    # expression for item in collection if condition
    return [num for num in lst if num % 2 == 0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens_lst = get_evens(lst)
print(evens_lst)