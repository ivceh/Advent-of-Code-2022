def priority(letter):
    if 'A' <= letter <= 'Z':
        return ord(letter) - ord('A') + 27
    elif 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    else:
        raise ValueError("Argument should be letter, not " + letter + "!")

def day03(infile):
    with open(infile, "r") as file:
        rucksack = file.read().splitlines()

    s1 = s2 = 0
    for line in rucksack:
        l = len(line)
        set1 = set(list(line[:l // 2]))
        set2 = set(list(line[l // 2:]))
        for lt in set1:
            if lt in set2:
                s1 += priority(lt)

    # solving Part One
    print("Part One: ", s1)

    for cnt in range(0, len(rucksack), 3):
        a = set(list(rucksack[cnt]))
        b = set(list(rucksack[cnt + 1]))
        c = set(list(rucksack[cnt + 2]))
        for l in a:
            if l in b and l in c:
                s2 += priority(l)

    # solving Part Two
    print("Part Two: ", s2)