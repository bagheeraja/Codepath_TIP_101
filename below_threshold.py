def count_less_than(numbers: [list], threshold: [int]):
    # return the number of items in numbers that are less than threhsold
    # list comprehension expression for item in list
    return [num for num in numbers if num < threshold]

numbers = [12, 8, 2, 4, 4, 10]
counter = count_less_than(numbers, 5)

print(counter)