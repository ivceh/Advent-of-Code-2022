def score(shape, outcome):
    return shape + 3 * outcome

def day04(infile):
    with open(infile, "r") as file:
        A = file.read().splitlines()

    s1 = s2 = 0
    for line in A:
        elf1, elf2 = line.split(",")
        l1, h1 = elf1.split("-")
        l2, h2 = elf2.split("-")
        l1 = int(l1)
        h1 = int(h1)
        l2 = int(l2)
        h2 = int(h2)
        if l1 <= l2 <= h2 <= h1 or l2 <= l1 <= h1 <= h2:
            s1 += 1

        if h1 >= l2 and h2 >= l1:
            s2 += 1

    # solving Part One
    print("Part One: ", s1)

    # solving Part Two
    print("Part Two: ", s2)