from itertools import compress

def factors(n):
    while n > 1:
        #for i in range(2, int(n**0.5)+1):
        for i in range(2, n+1):
            if n % i == 0:
                n = n // i
                yield i
                break

def proper(maxd):
    for d in range(2, maxd):
        proper = [True] * d
        for f in factors(d):
            proper[::f] = [False] * (d // f)
        for n in compress(range(len(proper)), proper):
            yield (n, d)

def main():
    # 1000000
    #for n, d in proper(1000001):
    #    print("{}/{}".format(n, d))
    print(len(list(proper(1000001))))

main()
