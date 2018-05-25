from itertools import count, combinations, cycle, islice, permutations, product

# Called PELL EQUATION

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

#@Memoize
#def isqrt(n):
#    x = n
#    y = (x + 1) // 2
#    while y < x:
#        x = y
#        y = (x + n // x) // 2
#    return x

#def is_square(i):
#    tmp = isqrt(i)
#    if tmp * tmp == i and tmp > 0:
#        return tmp
#    return None

#@Memoize
#def is_square(apositiveint):
#    if apositiveint == 1:
#        return 1
#    x = apositiveint // 2
#    seen = set([x])
#    while x * x != apositiveint:
#        x = (x + (apositiveint // x)) // 2
#        if x in seen:
#            return False
#        seen.add(x)
#    return True

import math
def is_square(integer):
    root = math.sqrt(integer)
    return int(root + 0.5) ** 2 == integer


def find_m(a, b, k, D):
    for m in count(int(math.sqrt(D))):
        if (a + b*m) % k == 0:
            return m


def substitute(a, b, k, D, m):
    return (a*m + D*b) // abs(k), (a + b*m) // abs(k), (m*m - D) // k


def initial(D):
    a = 1
    b = 1
    k = a*a - D * b * b
    return a, b, k


def chakravala(D):
    a, b, k = initial(D)
    while k != 1:
        m = find_m(a, b, k, D)
        a, b, k = substitute(a, b, k, D, m)
    return a, b, k


def diophantine_slow(D):
    """Iterates x and try to find y satifying x**2 - D * y**2 == 1"""
    print("D: {}".format(D))
    x = 1
    for i in cycle((D//2 - 2 if D % 2 == 0 else D - 2, 2)):
        x += i
        yy = (x*x - 1) // D
        if yy > 0 and is_square(yy):
            yield D, x, yy


def all_solutions_for_D_up_to(n):
    for D in range(2, n+1):
        if not is_square(D):
            x, y, k = chakravala(D)
            #print(x, y)
            yield D, x, y


def main():
    def x(solution):
        _, x, _ = solution
        return x

    #print(chakravala(61))
    #n = 7
    n = 1000
    D, x, y = max(all_solutions_for_D_up_to(n=n), key=x)
    print("D: {}, x: {}".format(D, x))

main()
