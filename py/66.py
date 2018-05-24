from itertools import count, cycle

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


def chakravala():
    pass


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
            solution = next(diophantine_slow(D))
            print(solution)
            yield solution

def main():
    def x(solution):
        _, x, _ = solution
        return x

    #n = 7
    n = 60
    D, x, y = max(all_solutions_for_D_up_to(n=n), key=x)
    print("D: {}, x: {}".format(D, x))

main()
