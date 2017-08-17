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
        #for p in self.primes:
        #    if p == n:
        #        return True
        #    if n % p == 0:
        #        return False
        # 
        #for i in range(self.primes[-1], n // 2):
        #    if n % i == 0:
        #        return False
        # 
        #self.primes.append(n)
        #self.primes.sort()
        for i in range(2, int(n**0.5) + 1):
            if n % i==0:
                return False

        return True

    def iter(self):
        for i in itertools.count():
            if self.is_prime(i):
                yield i
