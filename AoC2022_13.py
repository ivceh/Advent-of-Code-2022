from functools import cmp_to_key

def cmp(l1, l2):
    for el1, el2 in zip(l1, l2):
        if isinstance(el1, int):
            if isinstance(el2, int):
                if el1 < el2:
                    return -1
                elif el1 > el2:
                    return 1
            else:
                val = cmp([el1], el2)
                if val != 0:
                    return val
        else:
            if isinstance(el2, int):
                val = cmp(el1, [el2])
                if val != 0:
                    return val
            else:
                val = cmp(el1, el2)
                if val != 0:
                    return val
    if len(l1) < len(l2):
        return -1
    elif len(l1) > len(l2):
        return 1
    else:
        return 0

def day13(infile):
    # reading input
    with open(infile, "r") as file:
        A = file.read().splitlines()

    # solving Part One
    s1 = 0
    for i in range(0, len(A), 3):
        l1 = eval(A[i])
        l2 = eval(A[i + 1])
        if cmp(l1, l2) == -1:
            s1 += i // 3 + 1

    print("Part One: ", s1)

    # solving Part Two
    packets = []
    for line in A:
        if line != '':
            packets.append(eval(line))
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(cmp))

    print("Part Two: ", (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))