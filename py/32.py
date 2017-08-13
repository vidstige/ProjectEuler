from itertools import permutations

def _splits(length, n, result):
    if n == 1:
        yield tuple(result + [length])

    for head in range(1, length):
        for x in _splits(length-head, n-1, result + [head]):
            yield x

def splits(length, n):
    """Partitions the length in n pieces, all larger than one"""
    return _splits(length, n, [])


precalc = list(splits(9, 3))
products = set()
for y in permutations('123456789'): 
    x = ''.join(y)
    for p1, p2, p3 in precalc:
        a = int(x[:p1])
        b = int(x[p1:p1+p2])
        c = int(x[p1+p2:p1+p2+p3])
        if a * b == c:
            products.add(c)
            print("{} x {} = {}".format(a, b, c))

print(sum(products))
