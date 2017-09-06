import prime

def digits(n):
    while n >= 10:
        yield n % 10
        n = n // 10
    yield n

def main():
    primes = [p for p in prime.sieve(10000) if p > 1000]
    print(primes)
    for a in primes:
        for b in primes:
            step = b - a
            c = b + step
            if step > 0 and c in primes:
                da = sorted(digits(a))
                db = sorted(digits(b))
                dc = sorted(digits(c))
                if da == db and db == dc:
                    print(a, b, c)
            
    

main()
