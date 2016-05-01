from __future__ import print_function

solutions = {}
for p in xrange(0, 1000):
    #print("--- {} --------------".format(p))
    count = 0
    for a in xrange(1, p):
        for b in xrange(a, p - a):
            c = p - a - b
            if a*a + b*b == c*c:
                #print("{} {} {}".format(a,b,c))
                count = count + 1
                #print("YES")
    solutions[p] = count
    
print(max(solutions, key=solutions.get))