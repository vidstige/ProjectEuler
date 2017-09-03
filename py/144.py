from operator import sub
from math import pi

import numpy as np
import matplotlib.pyplot as plt

TAU = pi * 2

class Ellipse(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def point(self, t):
        return np.vstack((self.a * np.cos(t * TAU), self.b * np.sin(t * TAU)))

    def normal(self, p):
        return normal(np.array((p[0] / self.a**2, p[1] / self.b**2)))


def reflect(v, n):
    return v - 2 * np.dot(v, n) * n

def norm(p):
    return np.sqrt(p[0]*p[0] + p[1]*p[1])

def normal(p):
    n = norm(p)
    return np.array((p[0] / n, p[1] / n))


class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def point(self, t):
        return np.array((self.origin[0] + self.direction[0] * t,
                         self.origin[1] + self.direction[1] * t))

def intersection(ray, ellipse, tmin=0):
    dx, dy = ray.direction
    ox, oy = ray.origin
    a2 = ellipse.a ** 2
    b2 = ellipse.b ** 2

    a = b2 * dx**2 + a2 * dy**2
    b = 2*b2*ox*dx + 2*a2*oy*dy
    c = b2*ox**2 + a2*oy**2 - a2*b2

    D = b**2 / (4*a**2) - c / a
    if D < 0:
        return None

    t1 = -0.5 * b/a + np.sqrt(D)
    t2 = -0.5 * b/a - np.sqrt(D)

    return next((ray.point(t) for t in [t1, t2] if t >= tmin), None)


def minus(a, b):
    return tuple(map(sub, a, b))

def main():
    e = Ellipse(5, 10)
    #ray = Ray((0.0, 10.1), normal(minus((1.4,-9.6), (0.0, 10.1))))
    #print(ray.direction)
    #print(intersection(ray, e))
   
    #t = np.arange(0.0, 1.0, 0.02)
    #points = e.point(t)
    #x, y = points
    #plt.plot(x, y)
    #plt.axis('equal')


    ray = Ray(np.array((0.0, 10.1)), normal(np.array((1.4,-9.6)) - np.array((0.0, 10.1))))
    trace = [ray.origin]
    while ray.origin[0] < -0.01 or ray.origin[0] > 0.01 or ray.origin[1] < 0 or ray.origin[1] == 10.1:
        p = intersection(ray, e, 0.2)
        if p is not None:
            trace.append(p)
            ray = Ray(p, reflect(ray.direction, e.normal(p)))
        else:
            break
    
    #print("--trace--")
    print(len(trace) - 2)
    #print(trace[-1])
    #plt.plot(*zip(*trace))

    #plt.show()

main()
