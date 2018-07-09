from random import Random

GO = 0
JAIL = 10
GO2JAIL = 30
CC = (2, 17, 33)
CH = (7, 22, 36)
C1 = 11
E3 = 24
H2 = 39
R1 = 5
R = (5, 15, 25, 35)
U = (12, 28)

def double(roll):
    return len(set(roll)) == 1

def simulate(r, die):
    stops = [0] * 40

    p = GO  # start at GO
    consecutive_doubles = 0

    comunity_chest = list(range(16))
    r.shuffle(comunity_chest)
    cc = 0
    
    chance = list(range(16))
    r.shuffle(chance)
    ch = 0

    for _ in range(1000000):
        roll = tuple(r.randint(1, sides) for sides in die)
        p = (p + sum(roll)) % 40
        if double(roll):
            consecutive_doubles += 1
        else:
            consecutive_doubles = 0
        
        if consecutive_doubles == 3:
            p = JAIL
        if p == GO2JAIL:
            p = JAIL
        if p in CC:
            card = comunity_chest[cc]
            cc = (cc + 1) % len(comunity_chest)
            if card == 1:
                p = GO
            if card == 2:
                p = JAIL
            
        if p in CH:
            card = comunity_chest[cc]
            ch = (ch + 1) % len(chance)
            if card == 1:
                p = GO
            if card == 2:
                p = JAIL
            if card == 3:
                p = C1
            if card == 4:
                p = E3
            if card == 5:
                p = H2
            if card == 6:
                p = R1
            if card == 7:
                #Go to next R (railway company)
                p = next((r for r in R if r > p), R[0])
            if card == 8:
                # Go to next R
                p = next((r for r in R if r > p), R[0])
            if card == 9:
                # Go to next U (utility company)
                p = next((u for u in U if u > p), U[0])
            if card == 10:
                # Go back 3 squares.
                p = (p + 37) % 40

        stops[p] += 1

    return stops

def main():
    r = Random()
    r.seed(1337)

    #stops = simulate(r, (6, 6))
    stops = simulate(r, (4, 4))


    #total = sum(stops)
    #print([format(100 * s / total, '.2f') for s in stops])
    
    top_indices = sorted(range(len(stops)), key=lambda x: stops[x])[-3:]
    print("".join(format(i, '02') for i in reversed(top_indices)))

main()
