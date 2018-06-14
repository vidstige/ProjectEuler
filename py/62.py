from collections import Counter
from itertools import count, groupby, permutations, islice

def main(wanted):
    cubes = (i**3 for i in count())
    groups = groupby(cubes, lambda x: len(str(x)))
    for cc, g in groups:
        mapping = {x: ''.join(sorted(str(x), reverse=True)) for x in g}
        counts = Counter(mapping.values())
        for value, c in counts.items():
            if c == wanted:
                return min([k for k, v in mapping.items() if v == str(value)])


print(main(5))
