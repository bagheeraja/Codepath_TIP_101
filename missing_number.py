def find_missing(nums: [list]):
    nums.sort()
    n = len(nums)

    # the expected sum minus the actual sum will be the missing number
    actual_sum = sum(nums)
    expected_sum = n * (n + 1) // 2

    missing = expected_sum - actual_sum

    return missing

def find_missing_iter(nums: [list]):
    nums.sort()

    for i in range(len(nums)):
        if i != nums[i]:
            return i
        
def find_missing_enum(nums: [list]):
    
    for i, num in enumerate(nums):
        if i != num:
            return i

nums = [2,4,1,0,5,3,6,10,9,8]
missing_num = find_missing(nums)
print(missing_num)

missing_num2 = find_missing_iter(nums)
print(missing_num2)

missing_num3 = find_missing_enum(nums)
print(missing_num3)

print(1^2^1)