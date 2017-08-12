#ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
def main():
    terms = set()
    for a in range(2, 100+1):
        for b in range(2, 100+1):
            terms.add(a**b)
    return len(terms)

print(main())