def move_zeroes(nums: list[int]) -> list[int]:
    write = 0
    for num in nums:
        if num != 0:
            nums[write] = num
            write += 1
    while write < len(nums):
        nums[write] = 0
        write += 1

    return nums

def move_zeroes_comprehension(nums: list[int]) -> list[int]:
    non_zeroes = [x for x in nums if x != 0]
    zeroes = [x for x in nums if x == 0]
    return non_zeroes + zeroes


nums = [1, 0, 2, 3, 0, 0, 4]
new_nums = move_zeroes(nums)
print(new_nums)

new_nums2 = move_zeroes_comprehension(nums)
print(new_nums2)