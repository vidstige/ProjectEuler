import bisect
import itertools

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
        self.primes = [False, False]
        self.limit = 2

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
        return self.cache[n]
        

    def iter(self):
        for i in itertools.count():
            if self.is_prime(i):
                yield i
