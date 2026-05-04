def fizzbuzz(n: int):
    # multiples of 3 print "Fizz"
    # multiples of 5 print "Buzz"

    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    
fizzbuzz(13)