def day08(infile):
    # reading input
    with open(infile, "r") as file:
        A = [[int(c) for c in line] for line in file.read().splitlines()]
    m = len(A)
    n = len(A[0])

    # solving Part One
    visible = [[False] * n for _ in range(m)]

    # from left
    for i in range(m):
        height = -1
        for j in range(n):
            if A[i][j] > height:
                visible[i][j] = True
                height = A[i][j]
    # from right
    for i in range(m):
        height = -1
        for j in range(n - 1, -1, -1):
            if A[i][j] > height:
                visible[i][j] = True
                height = A[i][j]
    # from up
    for i in range(n):
        height = -1
        for j in range(m):
            if A[j][i] > height:
                visible[j][i] = True
                height = A[j][i]
    # from down
    for i in range(n):
        height = -1
        for j in range(m - 1, -1, -1):
            if A[j][i] > height:
                visible[j][i] = True
                height = A[j][i]

    print("Part One: ", sum(sum(row) for row in visible))

    # solving Part Two
    max_score = 0
    for i in range(m):
        for j in range(n):
            l = 0
            for k in range(j - 1, -1, -1):
                l += 1
                if A[i][k] >= A[i][j]:
                    break
            r = 0
            for k in range(j + 1, n):
                r += 1
                if A[i][k] >= A[i][j]:
                    break
            u = 0
            for k in range(i - 1, -1, -1):
                u += 1
                if A[k][j] >= A[i][j]:
                    break
            d = 0
            for k in range(i + 1, m):
                d += 1
                if A[k][j] >= A[i][j]:
                    break
            if l * r * u * d > max_score:
                max_score = l * r * u * d

    print("Part Two: ", max_score)