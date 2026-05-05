def get_odds(nums: list[int]) -> list[int]:
    odds_lst = []
    
    for num in nums:
        if num % 2 != 0:
            odds_lst.append(num)

    return odds_lst

def get_odds_comprehension(nums: list[int]) -> list[int]:
    # list comprehension is expression for item in collection condition
    odds_lst2 = []

    return [num for num in nums if num %2 != 0]

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)

odd_nums2 = get_odds_comprehension(nums)
print(odd_nums2)