def score(shape, outcome):
    return shape + 3 * outcome

def day02(infile):
    with open(infile, "r") as file:
        game = file.read().splitlines()

    s1 = s2 = 0
    for line in game:
        α = ord(line[0]) - ord('A')
        β = ord(line[2]) - ord('X')
        s1 += score(shape=β + 1, outcome=(β + 4 - α) % 3)
        s2 += score(outcome=β, shape=(β + α + 2) % 3 + 1)

    # solving Part One
    print("Part One: ", s1)

    # solving Part Two
    print("Part Two: ", s2)