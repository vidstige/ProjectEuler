#import functools

#@functools.lru_cache(maxsize=None)
#def is_prime(n):
#    for i in range(2, n // 2):
#        if n % i == 0:
#            return False
#    return True

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

def digits(n):
    while n >= 10:
        yield n % 10
        n = n // 10
    yield n

def rotate(l, n):
    return l[n:] + l[:n]

def to_int(int_list):
    r = 0
    p = 1
    for i in range(len(int_list)-1, -1, -1):
        r += int_list[i] * p
        p *= 10
    return r

def yield_rotations(n):
    dgts = list(digits(n))
    for i in range(len(dgts)):
        yield to_int(rotate(dgts, i))

def main():
    prime = Prime()
    for n in range(2, 1000000):
        if all(prime.is_prime(x) for x in yield_rotations(n)):
            print(n)
    #print(prime.primes)

main()
