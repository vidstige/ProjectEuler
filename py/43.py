from itertools import permutations

def iter_pandigitals(first, last):
        for x in permutations(list(range(first, last+1))):
            yield int(''.join(map(str, x)))

def main():
    parts = [
        (1,  4, 2),
        (2,  5, 3),
        (3,  6, 5),
        (4,  7, 7),
        (5,  8, 11),
        (6,  9, 13),
        (7, 10, 17),
    ]
    for p in iter_pandigitals(0, 9):
        s = str(p)
        if all(int(s[a:b]) % d == 0 for a,b,d in parts):
            print(p)

main()
