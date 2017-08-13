from math import factorial

def digits(n):
    while n >= 10:
        yield n % 10
        n = n // 10
    yield n

def main():
    for i in range(10, 10000000):
        if sum(factorial(d) for d in digits(i)) == i:
            print(i)

main()
