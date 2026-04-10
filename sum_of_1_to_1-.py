def sum_ten():
    sum = 0
    for i in range(11):
        sum += i
        i += 1
    return sum

output = sum_ten()
print(output)