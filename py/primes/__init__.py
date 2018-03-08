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
        self.primes = [2]
        self.cache = {}

    def is_prime(self, n: int) -> bool:
        if n not in self.cache:
            self.cache[n] = self._is_prime(n)
        return self.cache[n]

    def _is_prime(self, n: int) -> bool:
        if n == 1:
            return False
        for p in self.primes:
            if n == p:
                return True
            if n % p == 0:
                return False
         
        for i in range(self.primes[-1] + 1, n // 2):
            if n % i == 0:
                return False

        self.primes.append(n)
        self.primes.sort()
        return True

        #for i in range(2, int(n**0.5) + 1):
        #    if n % i==0:
        #        return False
        # 
        #return True

    def iter(self):
        for i in itertools.count():
            if self.is_prime(i):
                yield i
