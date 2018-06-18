def load():
    with open('p081_matrix.txt') as f:
        m = {}
        for y, line in enumerate(f):
            for x, value in enumerate(line.split(',')):
                m[(x, y)] = int(value)
        return m

def x_range(m):
    xs = [x for x, _ in m]
    return range(min(xs), max(xs) + 1)

def y_range(m):
    ys = [y for _, y in m]
    return range(min(ys), max(ys) + 1)

def search(m):
    c = {}
    for x in reversed(x_range(m)):
        for y in reversed(y_range(m)):
            options = [c.get((x + 1, y)), c.get((x, y + 1))]
            step = min([o for o in options if o is not None] or [0])
            c[(x, y)] = m.get((x, y)) + step
    print(c)
    #print(c[(0, 0)])

def main():
    m = load()
    search(m)

main()
