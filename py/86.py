from itertools import count, combinations

def search(M):
    squares = [i*i for i in range(1, 5)]
    for c in combinations(squares, 3):
        print(c)
    
def length(a, b, c):
    return a + b + c

def main():
    print(length(3, 5, 6))
    #print(search(M=100))

main()
