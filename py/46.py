from itertools import count
from primes import is_prime

def odd(n):
    return n % 2 == 1


def composites():
    return (i for i in count(4) if not is_prime(i))


def goldbach(n):
    """Tries to find a number s so that n = p + 2*s^2, where p is a prime"""
    for s in range(n):
        p = n - 2*s*s
        if is_prime(p):
            return s
    return None
    
def main():
    odd_composites = (c for c in composites() if odd(c))
    print(next(c for c in odd_composites if goldbach(c) is None))

main()
