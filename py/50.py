import prime

def consecutive_sum_primes(n):
    primes = prime.sieve(n)
    for i in range(len(primes)):
        s = 0
        c = i
        while s < n and c < len(primes):
            s += primes[c]
            c += 1
            if s in primes:
                yield (s, c - i)


def main():
    #n = 1000
    n = 1000000
    print(max(consecutive_sum_primes(n), key=lambda x: x[1]))

main()
