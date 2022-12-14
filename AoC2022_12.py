from collections import deque

def neighbours(climbing_criteria):
    def f(p):
        x, y = p
        for i, j in ((x, y - 1), (x, y + 1),
                     (x - 1, y), (x + 1, y)):
            if 0 <= i < len(A) and 0 <= j < len(A[0]):
                h = h_char_to_int(A[x][y])
                h2 = h_char_to_int(A[i][j])
                if climbing_criteria(h, h2):
                    yield i, j
    return f

def h_char_to_int(c):
    if c == 'S':
        c = 'a'
    elif c == 'E':
        c = 'z'
    return ord(c)

def cost(p, p2):
    x, y = p
    x2, y2 = p2
    h = h_char_to_int(A[x][y])
    h2 = h_char_to_int(A[x2][y2])
    if h2 > h + 1:
        return float("inf")
    else:
        return 1

# breadth first search
# input: function for neighbours of arbitrary point, start,
#        function that returns True if end criteria is met
# output: minimal number of steps from start to end
def bfs(neighbours, start, end_criteria):
    Q = deque([(start, 0)])
    visited = {start}
    while Q:
        p, dist = Q.popleft()
        for p2 in neighbours(p):
            if p2 not in visited:
                if end_criteria(p2):
                    return dist + 1
                Q.append((p2, dist + 1))
                visited.add(p2)

def day12(infile):
    # reading input
    with open(infile, "r") as file:
        global A
        A = file.read().splitlines()

    for i, line in enumerate(A):
        for j, c in enumerate(line):
            if c == 'S':
                sx, sy = i, j
            elif c == 'E':
                ex, ey = i, j

    # solving Part One
    print("Part One: ", bfs(neighbours(lambda h, h2: h2 <= h + 1),
                            (sx, sy),
                            lambda pos: A[pos[0]][pos[1]] == 'E'))

    # solving Part Two
    print("Part Two: ",bfs(neighbours((lambda h, h2: h2 >= h - 1)),
                           (ex, ey),
                           (lambda pos: A[pos[0]][pos[1]] == 'a')))