from collections import defaultdict
from itertools import combinations, permutations, islice, count
from primes import Prime

_cache = {}


def concatable_prime(p, a, b):
    if (a, b) not in _cache:
        x = p.is_prime(int('{}{}'.format(a, b))) and p.is_prime(int('{}{}'.format(b, a)))
        _cache[(a, b)] = x
        _cache[(b, a)] = x
    return _cache[(a, b)]


def concatable_primes(p, t):
    for a, b in combinations(t, 2):
        yield concatable_prime(p, a, b)


def search(p: Prime, t: tuple, r: int, first: int):
    if len(t) < r:
        for i, p1 in enumerate(islice(p.primes(), first, 2000)):
            t1 = t + (p1,)
            if all(concatable_primes(p, t1)):
                search(p, t1, r, first=i)
    else:
        print(t)


def main():
    p = Prime()
    p.sieve(100000000)
    primes = p.primes()
    print("sieve done")

    search(p, tuple(), 5, 0)

    print(p.counter)
    #graph = defaultdict(list)
    #for a, b in permutations(islice(primes, 100), 2):
    #    if concatable_prime(p, a, b):
    #        graph[a].append(b)

    #dfs(graph, 3, print)
    
    #for i, t in enumerate(combinations(primes, 4)):
    #    if i % 13001 ==0:
    #        print(t, end="\r")
    #    if all(concatable_primes(p, t)):
    #        print(t)

main()
