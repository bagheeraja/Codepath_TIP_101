def print_odd_indices(nums: list[int]) -> None:
    for i in range(len(nums)):
        if i % 2 != 0:
            print(nums[i])

def print_odd_indices_enum(nums: list[int]) -> None:
    for i, n in enumerate(nums):
        if i % 2 != 0:
            print(n)

nums = [3,4,8,1,5,2]
print_odd_indices(nums)
print_odd_indices_enum(nums)
