from itertools import permutations, islice

def nth(iterable, n):
    return next(islice(iterable, n, n + 1))

def main():
    print(''.join(nth(permutations('0123456789'), 1000000-1)))

main()
