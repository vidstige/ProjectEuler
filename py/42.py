def slurp(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def value(word):
    return sum(ord(c)-64 for c in word)

def is_triangle(n):
    for i in range(n+1):
        if 2*n == i*(i+1):
            return True
    return False

def count(iter):
    return sum(1 for _ in iter)

def main():
    words = [word.strip('"') for line in slurp('words.42.txt') for word in line.split(',')]
    print(count(word for word in words if is_triangle(value(word))))

main()
