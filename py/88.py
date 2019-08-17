from itertools import combinations
from functools import reduce
from operator import mul
from primes import Prime

prime = Prime()
prime.sieve(12000)

def product(parts):
    return reduce(mul, parts, 1)

def min_product_sum(k):
    for t in combinations(prime.primes(), k):
        print(t)
        if product(t) == sum(t):
            return sum(t)


def main():
    for k in range(2, 6):
        print(k, min_product_sum(k))

main()
