import itertools

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i==0:
            return False

    return True


class Prime(object):
    def __init__(self):
        self.primes = [2]

    def is_prime(self, n: int):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i==0:
                return False

        return True

    def iter(self):
        for i in itertools.count():
            if self.is_prime(i):
                yield i


def sieve(n: int):
    """"Returns list of all primes smaller or equal to n, in order"""
    marks = [True] * (n+1)
    marks[0] = False
    marks[1] = False
    p = 2
    while p*p < n:
        marks[2*p::p] = [False] * ((n-p) // p)
        p = marks.index(True, p) + 1

    return list(itertools.compress(range(len(marks)), marks))


def factors(n, primes=None):
    if not primes:
        primes = sieve(n)

    while n > 1:
        for p in primes:
            if n % p == 0:
                n = n // p
                yield p
                break