def prime_ser(number):
    for it in range(2, number):
        if prime(it) == True:
            print(it, end=" ")
        else:
            pass


number = int(input("add num"))
prime = lambda number: all(number % i != 0 for i in range(2, int(number ** .5) + 1))
print(prime)
