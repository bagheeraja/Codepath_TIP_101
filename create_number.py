def list_to_number(digits: list[int]) -> int:
    word = ""
    for num in digits:
        word += str(num)
    return int(word)


digits = [0, 0, 3]
number = list_to_number(digits)
print(number)