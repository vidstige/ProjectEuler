def grid(start, stop):
    for a in range(start, stop):
        for b in range(start, stop):
            yield (a, b)

def digital_sum(x):
    return sum(int(y) for y in str(x))

def main():
    m = max(digital_sum(a**b) for a, b in grid(1, 100))
    print(m)


main()
