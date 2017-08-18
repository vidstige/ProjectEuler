from itertools import compress

def sieve(n: int):
    """"Returns list of all primes smaller or equal to n, in order"""
    marks = [True] * (n+1)
    marks[0] = False
    marks[1] = False
    p = 2
    while p*p < n:
        marks[2*p::p] = [False] * ((n-p) // p)
        p = marks.index(True, p) + 1
    
    return list(compress(range(len(marks)), marks))

def factors(n, primes=None):
    if not primes:
        primes = sieve(n)

    while n > 1:
        for p in primes:
            if n % p == 0:
                n = n // p
                yield p
                break

def proper(maxd):
    primes = sieve(maxd)
    print("ok, got {} primes".format(len(primes)))
    for d in range(2, maxd):
        proper = [True] * d
        for f in factors(d, primes):
            proper[::f] = [False] * (d // f)
        for n in compress(range(len(proper)), proper):
            yield (n, d)
        #print(100 * d / maxd)

def main():
    # 1000000
    #for n, d in proper(1000001):
    #    print("{}/{}".format(n, d))
    print(len(list(proper(1000001))))
    #print(len(list(proper(9))))

main()
