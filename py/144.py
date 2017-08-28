from sympy.geometry import Ellipse, Point, Line, Ray, intersection
from sympy import simplify, symbols


def mirror(incoming: Ray, at: Point, normal: Line) -> Ray:
    return Ray(at, -incoming.direction.reflect(normal))


def normal(e: Ellipse, at: Point) -> Line:
    # TODO: This only works for (0, 0) centered ellipses
    return Line(Point(0, 0), Point(at.x / e.hradius**2, at.y / e.vradius**2))


def main():
    e = Ellipse(hradius=5, vradius=10)
    #x, y, z = symbols('x y z')
    ray = Ray(Point(0, 10.1), Point(1.4, -9.6))
    while True:
        all_intersections = intersection(ray, e)
        print(all_intersections)
        at = all_intersections[-1].evalf()
        print(at)
        if at.x > -0.01 and at.x < 0.01:
            print(at.x)
            print("bye, bye")

            break
        
        ray = mirror(ray, at, normal(e, at))

    #print([p.evalf() for p in intersection(ray, e)])

main()
