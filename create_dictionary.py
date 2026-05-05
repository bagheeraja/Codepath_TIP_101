def create_dictionary(keys: list[str], values: list[str]) -> dict[str,str]:
    if len(keys) != len(values):
        raise ValueError("keys and values must have the same length")
    
    output_dict = {}

    for i in range(len(keys)):
        output_dict[keys[i]] = values[i]

    return output_dict

def create_dictionary_enum(keys: list[str], values: list[str]) -> dict[str,str]:
    if len(keys) != len(values):
        raise ValueError("Keys and Values lists must have the same length")
    
    output_dict = {}
    
    for i, key in enumerate(keys):
        output_dict[key] = values[i]

    return output_dict

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']

print(create_dictionary(keys, values))
print(create_dictionary_enum(values, keys))