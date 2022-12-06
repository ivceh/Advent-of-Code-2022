def all_distinct(signal, end, length):
    return len(set(signal[end - length : end])) == length

def n_distinct_pos(signal, n):
    i = n
    while not all_distinct(signal, i, n):
        i += 1
    return i

def day06(infile):
    with open(infile, "r") as file:
        game = file.readline()

    # solving Part One
    print("Part One: ", n_distinct_pos(game, 4))

    # solving Part Two
    print("Part Two: ", n_distinct_pos(game, 14))