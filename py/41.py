from itertools import permutations
from prime import Prime

def iter_pandigitals():
    for n in range(2, 9+1):
        for x in permutations(list(range(1, n+1))):
            yield int(''.join(map(str, x)))

def main():
    prime = Prime()
    #print(prime.is_prime(987654321))
    print(max(p for p in iter_pandigitals() if prime.is_prime(p)))
    #for p in iter_pandigitals():
    #    print("{}: {}".format(p, prime.is_prime(p)))

main()
