def backwards(x):
    return int(''.join(reversed(str(x))))

def lychrel(x):
    n = x
    for _ in range(50):
        n = backwards(n) + n
        if backwards(n) == n:
            return False
    return True

def main():
    #print(lychrel(1))
    #print(lychrel(47))
    #print(lychrel(349))
    #print(lychrel(4994))
    print(sum(1 for x in range(1, 10000) if lychrel(x)))

main()
