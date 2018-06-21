# Outer cirles 0-4
# Inner circle 6-9
# First line 0-5-6
# Second 

def grouping(s):
    return (
        s[0], s[5], s[6],
        s[1], s[6], s[7],
        s[2], s[7], s[8],
        s[3], s[8], s[9],
        s[4], s[9], s[5])

def value(s):
    return "".join(str(x) for x in grouping(s))

def valid(s):
    """Checks so all lines evaluates to the same"""
    v = [
        s[0] + s[5] + s[6],
        s[1] + s[6] + s[7],
        s[2] + s[7] + s[8],
        s[3] + s[8] + s[9],
        s[4] + s[9] + s[5],
    ]
    return len(set(v)) == 1


def search(s, left):
    # Only search with minimal external node first
    if len(s) == 5 and s[0] != min(s):
        return

    if not left and valid(s):
        yield value(s)

    for i in range(len(left)):
        copy = left[:]
        v = copy.pop(i)
        yield from search(s + (v,), copy)

def main():
    for ring in search(tuple(), list(range(1, 10+1))):
        print(ring)

main()
