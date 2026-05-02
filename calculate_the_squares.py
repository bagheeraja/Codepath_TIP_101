def squares(nums: [list]):
    square_list = []

    for num in nums:
        square_list.append(num * num)

    return square_list

def squares_comprehension(nums: [list]):
    # new_list = [expression for item in collection]

    return [(num * num) for num in nums]


nums = [100, 200, 300, 400]

print(squares_comprehension(nums))