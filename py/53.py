def C(n, r):
    a = 1
    for x in range(r, n):
        a *= (x + 1)
    b = 1
    for x in range(n - r):
        b *= (x + 1)
    return a // b

def main():
    print(C(5, 3))
    print(C(23, 10))
    over = []
    for n in range(1, 100 + 1):
        for r in range(1, n - 1):
            c = C(n, r)
            if c > 1000000:
                over.append(c)
    #print(over)
    print(len(over))
    print(len(set(over)))

main()
