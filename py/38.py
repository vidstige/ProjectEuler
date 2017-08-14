from itertools import permutations, count

def digits(n):
    while n >= 10:
        yield n % 10
        n = n // 10
    yield n

def main():
    pandigital = set(int(''.join(x)) for x in permutations('123456789'))
    print("ok")
    for i in count():
        s = ''
        for j in range(1, 8):
            s += '{}'.format(i * j)
            if int(s) in pandigital:
                print(s)

main()
