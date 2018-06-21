from collections import Counter

def load():
    with open('p054_poker.txt') as f:
        for line in f:
            tmp = line.split()
            yield tuple(tmp[0:5]), tuple(tmp[5:10])

def suite(card):
    return card[1]

def value(card):
    return '123456789TJQKA'.index(card[0])

def royal(hand):
    return all(card[0] in 'TJQKA' for card in hand)

def flush(hand):
    return len(set(suite(card) for card in hand)) == 1

def straight(hand):
    values = [value(card) for card in hand]
    values.sort()
    return all(b - a == 1 for a, b in zip(values, values[1:]))

def high(hand):
    return tuple(sorted((value(card) for card in hand), reverse=True))

def rank(hand):
    count = Counter(value(card) for card in hand).items()
    #print(hand, count)
    if royal(hand) and flush(hand):
        print("ROYAL FLUSH")
        return (10,)
    if flush(hand) and straight(hand):
        print("STRAIGHT FLUHS")
        return (8,)
    if any(c for _, c in count if c == 4):
        print("FOUR OF A KIND")
        return (7,) + tuple(v for v, c in count if c == 1)
    pairs = sorted([v for v, c in count if c == 2])
    tripple = [v for v, c in count if c == 3]
    if pairs and tripple:
        print("Full house")
        return (6, tripple[0], pairs[0])
    if flush(hand):
        return (5, ) + high(hand)
    if straight(hand):
        return (4, ) + high(hand)
    if tripple:
        return (3, tripple[0])
    if len(pairs) == 2:
        return (2, pairs[1], pairs[0]) + high(hand)
    if pairs:
        return (1, pairs[0]) + high(hand)
    return (0,) + high(hand)

def main():
    print(sum(1 for a, b in load() if rank(a) > rank(b)))

main()
