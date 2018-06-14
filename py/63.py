def main():
    for x in range(1, 1000):
        for y in range(1, 100):
            n = x**y
            if len(str(n)) == y:
                print("{}={}**{}".format(n, x, y))
                

main()
