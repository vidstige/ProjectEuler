
def squares(d):
    width, height = d
    t = 0
    for w in range(width):
        for h in range(height):
            t += (w+1) * (h+1)
    return t

def main():
    target = 2000000
    best_d = target
    for w in range(1, 100):
        for h in range(1, 100):
            d = abs(target - squares((w, h)))
            if d < best_d:
                best_d = d
                best = (w, h)
    print(best, best_d)

main()
