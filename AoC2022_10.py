def cycle():
    global time, s1, x, B
    part = time % 40
    print(time)
    if x in (part - 1, part, part + 1):
        B[time] = '#'
    time += 1
    if time < 240 and time % 40 == 20:
        s1 += time * x

def day10(infile):
    # reading input
    with open(infile, "r") as file:
        A = file.read().splitlines()

    global time, s1, x, B
    s1 = 0
    x = 1
    B = ['.'] * 240
    time = 0
    for line in A:
        words = line.split(" ")
        inst = words[0]
        if inst == "addx":
            arg = int(words[1])
            cycle()
            cycle()
            x += arg
        elif inst == "noop":
            cycle()

    print("Part One: ", s1)

    print("Part Two: ")
    B = ''.join(B)
    for i in range(0, len(B), 40):
        print(B[i:i + 40])