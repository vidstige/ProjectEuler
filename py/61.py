from itertools import count, islice, dropwhile, takewhile, permutations

def replace_at_index(t: tuple, index: int, value) -> tuple:
    lst = list(t)
    lst[index] = value
    return tuple(lst)

def triangle(n): return n*(n+1)//2
def square(n): return n*n
def pentagonal(n): return n*(3*n-1)//2
def hexagonal(n): return n*(2*n-1)
def heptagonal(n): return n*(5*n-3)//2
def octagonal(n): return n*(3*n-2)

def fourdigit(s):
    return list(dropwhile(lambda i: i<999, takewhile(lambda i: i < 10000, s)))

def gen(f):
    return (f(i) for i in count())

def matches(a, b):
    """Checks if the last two digits of a matches the first two of b"""
    return str(a)[-2:] == str(b)[:2]

def search(sequences, i, trail):
    if i > len(sequences):
        if trail[-1] == trail[0]:
            print(sum(trail[1:]))
        return
    for item in sequences[len(sequences) - i - 1]:
        if not trail or matches(trail[-1], item):
            search(sequences, i + 1, trail + (item,))

def main():
    sequences = (
        fourdigit(gen(triangle)),
        fourdigit(gen(square)),
        fourdigit(gen(pentagonal)),
        fourdigit(gen(hexagonal)),
        fourdigit(gen(heptagonal)),
        fourdigit(gen(octagonal))
    )
    #sequences = (
    #    fourdigit(gen(triangle)), fourdigit(gen(square)), fourdigit(gen(pentagonal))
    #)

    for s in permutations(sequences):
        search(s, 0, tuple())

main()
