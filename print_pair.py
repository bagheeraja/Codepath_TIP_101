def print_pair(dictionary: dict[str, str], target: str) -> None:
    if dictionary.get(target):
        return f"Key: {target} \nValue: {dictionary[target]}"
    else:
        return "That pair does not exist."

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print(print_pair(dictionary, "patrick"))
print(print_pair(dictionary, "plankton"))
print(print_pair(dictionary, "spongebob"))