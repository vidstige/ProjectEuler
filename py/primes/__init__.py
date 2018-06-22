import bisect
import itertools
import math


class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

#@Memoize
def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i==0:
            return False

    return True


class Prime(object):
    def __init__(self):
        self._primes = None
        self.limit = 2

        self.counter = 0

    def sieve(self, limit):
        # Initialize the primality list
        self.cache = [True] * limit
        self.cache[0] = False
        self.cache[1] = False

        for (i, isprime) in enumerate(self.cache):
            if isprime:
                # Mark factors non-prime
                for n in range(i * i, limit, i):
                    self.cache[n] = False
        self.limit = limit

    def is_prime(self, n):
        if n < len(self.cache):
            return self.cache[n]
        
        self.counter += 1
        primes = self.primes()
        sqrtn = math.sqrt(n)
        if sqrtn < primes[-1]:
            for p in primes:
                if n % p == 0:
                    return False
                if p > sqrtn:
                    break
            return True

        raise Exception("Cannot determine primeness of {n}".format(n=n))

    def iter(self):
        for i in itertools.count():
            if self.is_prime(i):
                yield i

    def primes(self):
        if self._primes is None:
            self._primes = [i for i, b in enumerate(self.cache) if b]
        return self._primes

    def factor(self, n):
        idx = 0
        ps = self.primes()
        while n > 1:
            idx = next(i for i in itertools.count(idx) if n % ps[i] == 0)
            yield ps[idx]
            n //= ps[idx]
