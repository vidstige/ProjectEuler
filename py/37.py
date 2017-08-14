import itertools

class Prime(object):
    def __init__(self):
        self.primes = [2]

    def is_prime(self, n: int):
        if n == 1:
            return False
        for p in self.primes:
            if p == n:
                return True
            if n % p == 0:
                return False
        
        for i in range(self.primes[-1], n // 2):
            if n % i == 0:
                return False
        
        self.primes.append(n)
        return True

    def iter(self):
        for i in itertools.count():
            if self.is_prime(i):
                yield i

def trunc_iter(n):
    while n > 0:
        yield n
        n = n // 10


def trunc_left(n):
    s = str(n)
    for i in range(len(s)):
        yield int(s[i:])

def main():
    prime = Prime()
    total = []
    for p in prime.iter():
        right = all(prime.is_prime(x) for x in trunc_iter(p))
        left = all(prime.is_prime(x) for x in trunc_left(p))
        if right and left and p > 7:
            total.append(p)
            print(p)
            if len(total) == 11:
                break

    print("sum: {}".format(sum(total)))

main()
