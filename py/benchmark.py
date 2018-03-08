from primes import Prime, is_prime
import time

class Timer(object):
    def __init__(self, name):
        self.name = name
        self.t0 = None

    def __enter__(self):
        self.t0 = time.time()

    def __exit__(self ,type, value, traceback):
        t = time.time()
        dt = t - self.t0
        print("{}: {}".format(self.name, dt))


def main():
    p = Prime()
    n = 1000000
    sieve = [False] * n
    naive = [False] * n

    with Timer('naive'):
        for i in range(n):
            naive[i] = is_prime(i)

    with Timer('sieve'):
        p.sieve(n)
        for i in range(n):
            sieve[i] = p.is_prime(i)


main()
