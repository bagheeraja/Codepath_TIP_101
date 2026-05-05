def find_missing(nums: [list]):
    nums.sort()
    n = len(nums)

    # the expected sum minus the actual sum will be the missing number
    actual_sum = sum(nums)
    expected_sum = n * (n + 1) // 2

    missing = expected_sum - actual_sum

    return missing

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)

print(1^2^1)