from __future__ import print_function
from fractions import Fraction

def e(i):
    if i == 0:
        return None
    n = (i - 1) % 3
    return 1 if (n == 0 or n == 2) else ((i + 1) / 3) * 2   
    #e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

def estimate(s, f, j):
    def inner(i):
        if i == 0:
            return "1"
        #return Fraction(s, 1) + Fraction(s, inner(i - 1))
        return "{} + ({}/{})".format(s, s, inner(i - 1))
    return inner(j) 
    #if i == 0:
    #    return Fraction(s, 1)
    #return estimate(s, f, i - 1) + Fraction(s, f(i))
    #return Fraction(s, estimate())


# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
# 2
# 2 + 1/1
# 2 + 1/(1 + 1/2) = 2 + 2/3 = 8/3
# 2 + 1/(1 + 1/(2 + 1)) = 2 + 1/(4/3) = 8/4 + 3/4 = 11/4

for i in xrange(0, 10):
    print("{}: {}".format(i, estimate(1, lambda i: 2, i)))
#    print(e(i))

