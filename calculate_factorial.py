def factorial(n: [int]):
    acc = 1
    while n > 0:
        acc *= n
        n -= 1
    return acc

def factorial_for(n: [int]):
    acc = 1

    for i in range(1, n + 1):
        acc *= i
    
    return acc

print(factorial_for(5))