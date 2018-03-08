from primes import is_prime
from itertools import count, islice

# 2 3 5 7
def spirals():
    #sp = {}
    x, y = 0, 0
    dx, dy = 1, 0
    d = {
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
        (0, 1): (1, 0)
    }
    ds = {
        (1, 0): 0,
        (0, -1): 1,
        (-1, 0): 0,
        (0, 1): 1
    }
    s = 0
    c = 0
    diagonals = []
    for i in count(1):
        #sp[(x, y)] = i
        if x == y or -x == y:
            diagonals.append(i)

        x, y = x + dx, y + dy
        c += 1

        if c > s:
            if (dx, dy) == (1, 0):
                yield diagonals
                diagonals = []

            c = 0
            s += ds[(dx, dy)]
            dx, dy = d[(dx, dy)]

def get_ranges(spiral):
    x_range = range(
        min(x for _, x in spiral),
        max(x for _, x in spiral) + 1)
    y_range = range(
        min(y for _, y in spiral),
        max(y for _, y in spiral) + 1)
    return x_range, y_range

def print_spiral(spiral):
    x_range, y_range = get_ranges(spiral)
    for y in y_range:
        for x in x_range:
            i = spiral.get((x, y), 0)
            print("{: 3}".format(i), end='')
        print()

def diagonal(s):
    x_range, y_range = get_ranges(s)
    for x, y in zip(x_range, y_range):
        yield s[(x, y)]
    for x, y in zip(reversed(x_range), y_range):
        yield s[(x, y)]

def main():
    #for s, d in islice(spirals(), 3):
    #    print_spiral(s)
    #    print(d)
    #    print(list(sorted(diagonal(s))))
    #return None
    
    #primes = Prime()
    #is_prime = primes.is_prime

    primes = 0
    total = 0
    side_length = 1
    for diags in spirals():
        primes += sum(1 for i in diags if is_prime(i))
        total += len(diags)
        ratio = primes / total
        print(" {} {:.4f}".format(side_length, ratio), 
            end='\r')
        if ratio < 0.10 and ratio > 0:
            return
        side_length += 2
    print()

main()
