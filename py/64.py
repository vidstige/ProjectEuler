from itertools import count
import math

def continued_fraction(n):
    """Returns the continued fraction of sqrt(n)"""
    a0 = int(math.sqrt(n))
    a = a0
    b = a0
    up = 1
 
    f = []
    for _ in count():
        f.append((a, up, b))
        #print(a, up, b)
        up = (n - b*b) // up
        if up == 0:
            return None, None
        if up < 0:
            print("BOOM")
        a = (int(math.sqrt(n)) + b) // up
        if a == 0:
            a = 1
        b = a * up - b

        if (a, up, b) in f:
            return a0, tuple(t[0] for t in f[1:])


def is_odd(x):
    return x % 2 == 1


def main(N):
    #i, f = continued_fraction(30)

    c = 0
    for x in range(2, N+1):
        #print("  {}".format(x), end="\r")
        i, f = continued_fraction(x)
        if i is not None:
            #print("√{} = {}{} ({})".format(x, i, f, len(f)))
            if is_odd(len(f)):
                c += 1

    print(c)


#main(13)
main(10000)
