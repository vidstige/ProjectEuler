# 2 3 5 7
def spiral(n):
    sp = {}
    x, y = 0, 0
    dx, dy = 1, 0
    names = {
        (1, 0): 'right',
        (0, -1): 'up',
        (-1, 0): 'left',
        (0, 1): 'down'
    }
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
    for i in range(1, n * n + 1):
        if (x, y) in sp:
            print("ops")
        sp[(x, y)] = i
        x, y = x + dx, y + dy
        c += 1
        #print("{} then {}".format(i, names[(dx, dy)]))
        if c > s:
            # change direction
            c = 0
            s += ds[(dx, dy)]
            dx, dy = d[(dx, dy)]

    return sp

def print_spiral(spiral):
    y_range = range(
        min(y for _, y in spiral),
        max(y for _, y in spiral) + 1)
    x_range = range(
        min(x for _, x in spiral),
        max(x for _, x in spiral) + 1)
    for y in y_range:
        for x in x_range:
            i = spiral.get((x, y), 0)
            print("{: 3}".format(i), end='')
        print()

def main():
    s = spiral(7)
    print_spiral(s)

main()
