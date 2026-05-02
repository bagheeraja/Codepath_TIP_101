def halve_lst(lst):
    result = []

    for number in lst:
        halved = number/2
        result.append(round(halved))
    
    return result

halve_list = [2,4,6,8]
print(halve_lst(halve_list))
