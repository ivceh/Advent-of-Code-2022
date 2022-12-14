def rock_positions(A):
    rocks = set()
    for line in A:
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            x1, y1 = (int(c) for c in p1.split(","))
            x2, y2 = (int(c) for c in p2.split(","))
            if x1 == x2:
                if y1 < y2:
                    for y in range(y1, y2 + 1):
                        rocks.add((x1, y))
                else:
                    for y in range(y2, y1 + 1):
                        rocks.add((x1, y))
            elif x1 < x2:
                for x in range(x1, x2 + 1):
                    rocks.add((x, y1))
            else:  # x1 > x2
                for x in range(x2, x1 + 1):
                    rocks.add((x, y1))
    return rocks

def where_does_it_stop(point):
    x, y = point
    moved = True
    while moved:
        moved = False
        for pt in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1)):
            if y > 500:
                return None
            if pt not in taken:
                x, y = pt
                moved = True
                break
    return x, y


def day14(infile):
    # reading input
    with open(infile, "r") as file:
        A = file.read().splitlines()

    s1 = s2 = 0

    # solving Part One
    global taken
    taken = rock_positions(A)
    p = 1
    while p is not None:
        p = where_does_it_stop((500, 0))
        taken.add(p)
        s1 += 1

    print("Part One: ", s1 - 1)

    # solving Part Two
    maxy = max(max(int(pt.split(",")[1])
               for pt in line.split(" -> "))
               for line in A)
    A.append("0," + str(maxy + 2) + " -> " + "1000," + str(maxy + 2))
    taken = rock_positions(A)

    while p != (500, 0):
        p = where_does_it_stop((500, 0))
        taken.add(p)
        s2 += 1

    print("Part Two: ", s2)
