# Integer math functions
def product(v):
    r = 1
    for e in v:
        r *= e
    return r

def φ(n):
    factors = set(prime.factor(n))
    return n * product(f - 1 for f in factors) // product(factors)
