from itertools import count, islice
import prime

def window(seq, n):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def unique_factors(i, prime):
    return len(set(primes.factors(i, prime)))

def main():
    prime = primes.sieve(1000000)
    for t in window(count(2), 4):
        if all(unique_factors(i, prime) == 4 for i in t):
            print(t)
            break
        if t[2] > 1000000:
            print("oh noes")
            return
        

main()
