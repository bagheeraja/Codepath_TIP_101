def find_divisors(n: int):
    divisors = []
    
    for i in range (1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != (n // i):
                divisors.append(n // i)
    divisors.sort()
    return divisors

lst = find_divisors(6)
print(lst)

