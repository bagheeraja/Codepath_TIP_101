def keys_v_values(dictionary: dict[int, int]) -> str:
    keys_sum = sum(dictionary.keys())
    values_sum = sum(dictionary.values())
    
    # for key, value in dictionary.items():
    #     keys_sum += key
    #     values_sum += value

    if keys_sum > values_sum:
        return "keys"
    if keys_sum < values_sum:
        return "values"
    return "balanced"
    
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)