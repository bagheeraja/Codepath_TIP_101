def is_monotonic(nums: list) -> bool:
    # empty and single element lists are considered monotonic. Test for empty cases first to avoid ValueErrors.
    # Test for single element lists next.

    # zip() may be the better method to handle this. zip() will not return an error for empty or single element lists.
    # zip() basically assumes True for empty lists and single element lists

    # use two Boolean variables to track increasing and descreasing
    
    increasing = True
    decreasing = True

    for a, b in zip(nums, nums[1:]):
        if a > b:
            increasing = False
        if a < b:
            decreasing = False
        if not increasing and not decreasing:
            return False
    return True

        
nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))
