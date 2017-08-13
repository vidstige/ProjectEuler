from operator import mul
from functools import reduce
from fractions import gcd

def iter_quotes():
    for y1 in range(1, 10):
        for y2 in range(0, 10):
            for x1 in range(1, 10):
                for x2 in range(0, 10):
                    yield x1,x2, y1,y2

def qeq(a1, b1, a2, b2):
    """Returns whether the a1/b1 == a2/b2"""
    return a1*b2 == a2*b1

def check(x, y, a, b):
    if x >= y:
        return False
    if y % 10 == 0:
        return False
    return qeq(x, y, a, b)

def iter_curious():
    for x1, x2, y1, y2 in iter_quotes():
        x = x1 * 10 + x2
        y = y1 * 10 + y2
        if x1 == y1 and check(x, y, x2, y2):
            yield (x, y)
        if x1 == y2 and check(x, y, x2, y1):
            yield (x, y)
        if x2 == y1 and check(x, y, x1, y2):
            yield (x, y)
        if x2 == y2 and check(x, y, x1, y1):
            yield (x, y)

def main():
    curious = list(iter_curious())
    print(curious)
    a = reduce(mul, (aa[0] for aa in curious), 1)
    b = reduce(mul, (aa[1] for aa in curious), 1)

    print("{a} / {b}".format(a=a, b=b))
    print(a / gcd(a, b))
    print(b / gcd(a, b))
# 49 / 98 == 4/8
main()
