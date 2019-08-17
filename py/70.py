from fractions import Fraction
from itertools import combinations

from tqdm import tqdm
from primes import Prime

prime = Prime()
prime.sieve(10000000 // 2)
#prime.sieve(100000)

def product(v):
    r = 1
    for e in v:
        r *= e
    return r

def φ(n):
    factors = set(prime.factor(n))
    return n * product(f - 1 for f in factors) // product(factors)

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def quick_totients(rmax):
    for r in range(1, rmax):
        print(r)
        for factors in combinations(prime.primes(), r):
            product_factors = product(factors)
            totient = product(f - 1 for f in factors)
            if is_permutation(totient, product_factors):
                yield product_factors, totient

def main(n):
    def minimizer(pair):
        i, phi = pair
        return Fraction(i, phi)

    print('sieve done')
    print(min(quick_totients(3), key=minimizer))

main(n=10000000)
