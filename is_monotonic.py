def is_monotonic(nums: list) -> bool:
    # empty and single element lists are considered monotonic. Test for empty cases first to avoid ValueErrors.
    # Test for single element lists next.

    #zip() may be the better method to handle this. zip() will not return an error for empty or single element lists.
    
    # check first element to see if it is min or max of the list
    # if the list does not start with min or max it can't be monotonic

    # if first element is min save first element for comparison, pop first element while the list is not empty
    # if the list is empty after all items have been compared and popped it was monotonic

    # if first element is max save current element for comparison, pop element, compare while the list is not empty
    # if the list is empty after all items have bee compared and popped it was monotonic

    # if any of the comparisons fail, return False.
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
