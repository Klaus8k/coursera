import itertools


def primes():
    n = 1000
    a = range(n + 1)
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    yield lst





print(list(itertools.takewhile(lambda x : x <= 31, primes())))