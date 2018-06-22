from fractions import Fraction
from tqdm import tqdm
from primes import Prime

prime = Prime()
prime.sieve(1000000)

def product(v):
    r = 1
    for e in v:
        r *= e
    return r

def φ(n):
    factors = set(prime.factor(n))
    return n * product(f - 1 for f in factors) // product(factors)

def main(i):
    def maximizer(x):
        return Fraction(x, φ(x))
    print(max((n for n in tqdm(range(2, i+1))), key=maximizer))

main(1000000)
