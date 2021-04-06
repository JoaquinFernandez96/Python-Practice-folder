def sieve(n):
    primes = [True for i in range(n + 1)]
    for i in range(2, int((n ** 0.5)) + 1):
        if primes[i] == True:
            j = 0
            while ((i ** 2) + j * i) <= n:
                primes[(i ** 2) + j * i] = False
                j += 1
    primes[0] = False
    primes[1] = False
    return [k for k, x in enumerate(primes) if x == True]
