from collections import defaultdict
import math
from tqdm import tqdm

# 1500 -> 161
# 15000 -> 1663

def coprimes():
    yield 2, 1
    yield 3, 1
    for m, n in coprimes():
        yield 2*m - n, m
        yield 2*m + n, m
        yield m + 2*n, n


def farey(n):
    """Print the nth Farey sequence, either ascending or descending."""
    a, b, c, d = 0, 1, 1, n
    #yield a, b
    while (c <= n):
        k = (n + b) // d
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        yield a, b


def perfect_sqrt(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return None
        seen.add(x)
    return x


def count_triangles(L: int):
    counter = defaultdict(int)

    for n, m in farey(int(math.sqrt(L))):
        if m % 2 == 1 and n % 2 == 1:
            continue
        
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        circumference = a + b + c
        for overtone in range(circumference, L, circumference):
            counter[overtone] += 1

    return sum(1 for value, count in counter.items() if count == 1 and value < L)

def safe(n):
    # Precalculate squares
    sqrt = {}
    for i in range(1, 2*n):
        sqrt[i * i] = i
    
    counter = defaultdict(int)
    for a in range(1, n):
        for b in range(a, n):
            c = sqrt.get(a*a + b*b)
            if c:
                counter[a + b + c] += 1
    
    #for k in sorted(counter.keys()):
    #    print(k, counter[k])

    #print(max(counter))
    return sum(1 for value, count in counter.items() if count == 1 and value < n)


def main():
    import sys
    n = int(sys.argv[1])
    print('fast:', count_triangles(n))
    #print('safe:', safe(n))

main()
