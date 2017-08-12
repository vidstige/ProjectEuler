cache = {}
def pentagonal(n):
    p = int(n * (3 * n - 1) / 2)
    cache[p] = True
    return p 

for i in range(1, 10000):
    for j in range(i+1, 10000):
        pi = pentagonal(i)
        pj = pentagonal(j)
        if (pi + pj) in cache and (pj - pi) in cache:
            print("{} {} D={}".format(i, j, pj - pi))
        


