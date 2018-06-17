from itertools import count, islice
from fractions import Fraction

def approximate_e(n):
    def cf_e():
        for k in count(1):
            yield 1
            yield 2*k
            yield 1

    def fraction_part(cfs):
        if not cfs:
            return Fraction()
        return Fraction(1, cfs.pop(0) + fraction_part(cfs))

    cfs = list(islice(cf_e(), n - 1))
    return Fraction(2) + fraction_part(cfs)

def digits(x):
    return tuple(int(digit) for digit in str(x))

def main():
    e = approximate_e(100)
    print(e)
    print(sum(digits(e.numerator)))

main()
