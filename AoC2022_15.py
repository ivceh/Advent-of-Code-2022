import re

def dist1dim(x, y):
    return abs(x - y)

def manhattan(a, b):
    return sum(dist1dim(x, y) for x, y in zip(a, b))  #*zip?

def uv_from_xy(x, y):
    return x + y, x - y

def xy_from_uv(u, v):
    if (u - v) % 2 != 0:
        return None
    return (u + v) // 2, (u - v) // 2

def square_limits_uv(sensor, beacon):
    d = manhattan(sensor, beacon)
    u, v = uv_from_xy(*sensor)
    ulims = u - d, u + d + 1
    vlims = v - d, v + d + 1
    return ulims, vlims

def square_extreme_int_points(umin, umax, vmin, vmax):
    #print("*")
    rl = set()
    xy = xy_from_uv(umin, vmin)
    if xy is None:
        rl.add(xy_from_uv(umin + 1, vmin))
        rl.add(xy_from_uv(umin, vmin + 1))
    else:
        rl.add(xy)

    xy = xy_from_uv(umin, vmax - 1)
    if xy is None:
        rl.add(xy_from_uv(umin + 1, vmax - 1))
        rl.add(xy_from_uv(umin, vmax - 2))
    else:
        rl.add(xy)

    xy = xy_from_uv(umax - 1, vmin)
    if xy is None:
        rl.add(xy_from_uv(umax - 2, vmin))
        rl.add(xy_from_uv(umax - 1, vmin + 1))
    else:
        rl.add(xy)

    xy = xy_from_uv(umax, vmax - 1)
    if xy is None:
        rl.add(xy_from_uv(umax - 1, vmax - 1))
        rl.add(xy_from_uv(umax, vmax - 2))
    else:
        rl.add(xy)

    rl2 = set()
    for r in rl:
        x, y = r
        u, v = uv_from_xy(*r)
        if umin <= u < umax:
            if vmin <= v < vmax:
                if 0 <= x <= 4000000:
                    if 0 <= y <= 4000000:
                        rl2.add(r)

    return rl2

def day15(infile):
    # reading input
    A = []
    with open(infile, "r") as file:
        for line in file.read().splitlines():
            matchObj = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)',
                                line)
            A.append(((int(matchObj.group(1)), int(matchObj.group(2))),
                      (int(matchObj.group(3)), int(matchObj.group(4)))))

    s1 = s2 = 0

    # solving Part One
    y = 2000000 #y = 10 #
    S = []
    for sensor, beacon in A:
        d = manhattan(sensor, beacon)
        xs, ys = sensor
        dy = dist1dim(y, ys)
        if dy <= d:
            S.append((xs - (d - dy), 1))
            S.append((xs + (d - dy + 1), -1))
            #print((xs - (d - dy), (xs + (d + dy + 1))))
        #else:
            #print("not")
    S.sort()
    Ys = list({b[0] for a, b in A if b[1] == y})
    #print(Ys)
    #print()
    #print(S)

    i = 0
    cnt = 0
    prev = None
    for k, v in S:
        if prev is not None and cnt > 0:
            s1 += k - prev
            while i < len(Ys) and prev <= Ys[i] < k:
                s1 -= 1
                i += 1
        cnt += v
        prev = k

    print("Part One: ", s1)

    # solving Part Two
    print("Part Two: ", end=" ")

    squares = []
    B = []
    for sensor, beacon in A:
        squares.append(square_limits_uv(sensor, beacon))

    for ulims, vlims in squares:
        umin, umax = ulims
        B.append((umin, vlims, 1))
        B.append((umax, vlims, -1))
    B.sort()
    ucnt = 0
    prev = None
    for u, _, val in B:
        if prev is not None:
            C = []
            for ulims, vlims in squares:
                umin, umax = ulims
                #print(umin <= prev <= u <= umax, end=" ")
                if umin <= prev <= u <= umax:
                    vmin, vmax = vlims
                    C.append((vmin, 1))
                    C.append((vmax, -1))
            C.sort()
            #print()
            vcnt = 0
            prevv = None
            for v, val in C:
                #print(vcnt, end=" ")
                if prevv is not None and vcnt == 0:
                    for r in square_extreme_int_points(prev, u, prevv, v):
                        print(r[0] * 4000000 + r[1])
                vcnt += val
                prevv = v
            #print()
        ucnt += val
        prev = u