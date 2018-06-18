from typing import Tuple
Point = Tuple[int, int]


def sign(p1: Point, p2: Point, p3: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)


def contains(triangle, p):
    v1, v2, v3 = triangle
    b1 = sign(p, v1, v2) < 0
    b2 = sign(p, v2, v3) < 0
    b3 = sign(p, v3, v1) < 0

    return (b1 == b2) and (b2 == b3)

def pairwise(iterable):
    i = iter(iterable)
    return list(zip(i, i))

def load():
    with open('p102_triangles.txt') as f:
        for line in f:
            yield pairwise(int(x) for x in line.split(','))

def main():
    origo = (0, 0)
    #t1 = [(-340, 495), (-153, -910), (835,-947)]
    #t2 = [(-175,41), (-421,-714), (574,-645)]
    #print(contains(t1, origo))
    #print(contains(t2, origo))
    
    print(sum(1 for t in load() if contains(t, origo)))

main()
