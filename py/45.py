from itertools import count

def triangles():
    for n in count(1):
        yield n*(n+1) // 2

def pentagonals():
    for n in count(1):
        yield n*(3*n-1)//2

def hexagonals():
    for n in count(1):
        yield n*(2*n-1)

def tripplets():
    ts = triangles()
    ps = pentagonals()
    hs = hexagonals()

    t = next(ts)
    p = next(ps)
    h = next(hs)
    while True:
        if t == p and p == h:
            yield t
        m = min(t, p, h)
        if m == t:
            t = next(ts)
        elif m == p:
            p = next(ps)
        elif m == h:
            h = next(hs)

def main():
    for tripplet in tripplets():
        print(tripplet)

main()
