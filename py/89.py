def parse_roman(roman: str) -> str:
    """Returns the value of the roman string, or None if invalid"""
    n = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    v = 0
    p = None
    for c in roman:
        if p is not None and p < n[c]:
            v -= 2*p
        v += n[c]
        p = n[c]
        
    return v

def roman(x: int) -> str:
    numerals = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]
    result = []
    while x > 0:
        for c, v in numerals:
            while x >= v:
                x -= v
                result.append(c)
    return ''.join(result)

def main():
    saved = 0
    with open("roman.txt", "r") as f:
        for line in f:
            r = line.strip()
            v = parse_roman(r)
            saved += len(r) - len(roman(v))
        
    print(saved)
main()
