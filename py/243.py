from itertools import count, combinations
from fractions import Fraction, gcd

from tqdm import tqdm

from primes import Prime

prime = Prime()
prime.sieve(1000000)

def factor(n):
    idx = 0
    primes = prime.primes()
    while n > 1:
        idx = next(i for i in count(idx) if n % primes[i] == 0)
        yield primes[idx]
        n //= primes[idx]

def product(iterable):
    tmp = 1
    for x in iterable:
        tmp *= x
    return tmp

def facit(d):
    return sum(1 for n in range(1, d) if gcd(n, d) == 1)

def R(d):
    factors = set(factor(d))
    resilient = d
    s = -1
    for r in range(1, len(factors) + 1):
        resilient += s * sum(d // product(t) for t in combinations(factors, r))
        s *= -1
    #print(d, facit, resilient, factors)
    if resilient != facit(d):
        print("WRONG", d, resilient, facit(d))
    return Fraction(resilient, d-1)

def search(threshold):
    for d in tqdm(count(2)):
        if R(d) < threshold:
            return d


#R(2*2*3)
#R(2*3*5*7*11*13)
#print(search(Fraction(4, 10)))
print(search(Fraction(15499, 94744)))
