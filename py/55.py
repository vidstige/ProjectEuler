def palindromic(n: int) -> bool:
    s = str(n)
    return s[::-1] == s

def lychrel(n: int, iterations=50) -> bool:
    for _ in range(iterations):
        n = int(str(n)[::-1]) + n
        if palindromic(n):
            return False
    return True

def main():
    #print(lychrel(349))
    print([lychrel(x) for x in range(10000)].count(True))

main()
