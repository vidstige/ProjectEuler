from fractions import Fraction
import sys

def approximate_sqrt_2(n):
    def fraction_part(cfs):
        if not cfs:
            return Fraction()
        return Fraction(1, cfs.pop(0) + fraction_part(cfs))

    cfs = [2] * n
    return Fraction(1) + fraction_part(cfs)

def main():
    sys.setrecursionlimit(1500)
    aa = [approximate_sqrt_2(i) for i in range(1, 1000)]
    #print(aa)
    print(sum(1 for a in aa if len(str(a.numerator)) > len(str(a.denominator))))

main()
