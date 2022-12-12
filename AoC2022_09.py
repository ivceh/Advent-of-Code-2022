direction_vectors = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "⇧": (-1, 0),
    "⇩": (1, 0),
    "⇦": (0, -1),
    "⇨": (0, 1),
    "↖": (-1, -1),
    "↗": (-1, 1),
    "↙": (1, -1),
    "↘": (1, 1),
    "□": (0, 0)
}

moves = [
    "↘↘⇩↙↙",
    "↘□□□↙",
    "⇨□□□⇦",
    "↗□□□↖",
    "↗↗⇧↖↖"
]

def step_in_direction(pos, direction_symbol):
    dir_vec = direction_vectors[direction_symbol]
    x, y = pos
    dirx, diry = dir_vec
    return x + dirx, y + diry

def move_towards(my_pos, head_pos):
    my_x, my_y = my_pos
    head_x, head_y = head_pos
    delta_x = my_x - head_x
    delta_y = my_y - head_y
    return step_in_direction(my_pos, moves[delta_x + 2][delta_y + 2])

def day09(infile):
    # reading input
    with open(infile, "r") as file:
        A = file.read().splitlines()

    # solving Part One
    visited = set()
    head = tail = (0, 0)
    for line in A:
        direction, length = line.split(" ")
        for _ in range(int(length)):
            head = step_in_direction(head, direction)
            tail = move_towards(tail, head)
            visited.add(tail)

    print("Part One: ", len(visited))

    #solving Part Two
    visited = set()
    rope = [(0, 0) for _ in range(10)]
    for line in A:
        direction, length = line.split(" ")
        for _ in range(int(length)):
            rope[0] = step_in_direction(rope[0], direction)
            for i in range(1, 10):
                rope[i] = move_towards(rope[i], rope[i - 1])
            visited.add(rope[9])

    print("Part Two: ", len(visited))
