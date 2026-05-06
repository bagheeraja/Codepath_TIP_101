def sum_even_values(dictionary: dict[str,int]) -> int:
    sum_evens = 0
    
    return sum(value for value in dictionary.values() if type(value) is int and value % 2 == 0)

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))
